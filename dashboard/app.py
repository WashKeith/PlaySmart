"""
PlaySmart: Game Deal Price Tracker Dashboard
Interactive Streamlit dashboard for finding the best game deals and tracking prices
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from datetime import datetime
import warnings
import os

# Fix for Python 3.13 asyncio event loop issue
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"

warnings.filterwarnings("ignore")

# Page configuration
st.set_page_config(
    page_title="PlaySmart - Game Deal Tracker",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom styling - Gaming Theme
st.markdown(
    """
    <style>
    /* Modern Gaming Color Palette */
    .stApp {
        background-color: #0f1419;
        color: #e0e0e0;
    }

    body {
        background-color: #0f1419;
        color: #e0e0e0;
    }

    /* Headers */
    h1, h2, h3 {
        color: #00ff88;
        font-weight: 700;
    }

    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #1a2332 0%, #0f3460 100%);
        border: 1px solid #00ff88;
        border-radius: 10px;
        padding: 20px;
        color: #ffffff;
    }

    /* Deal quality badges */
    .deal-exceptional {
        background-color: #ff6b6b;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
    }

    .deal-excellent {
        background-color: #ffd93d;
        color: black;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
    }

    .deal-good {
        background-color: #6bcf7f;
        color: black;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #00ff88 0%, #00cc6a 100%);
        color: #000;
        border: none;
        border-radius: 8px;
        font-weight: 600;
    }

    /* Selectbox and inputs */
    .stSelectbox, .stDateInput, .stSlider {
        color: #e0e0e0;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1a2332;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #00ff88;
    }

    /* Info boxes */
    .stAlert {
        background-color: #1a3a3a;
        border-left: 4px solid #00ff88;
        color: #e0e0e0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_deals_data():
    """Load the latest processed deals data"""
    data_dir = Path(__file__).parent.parent / "processed_data"

    # Find the latest deals file
    deals_files = sorted(data_dir.glob("deals_processed*.csv"), reverse=True)

    if not deals_files:
        return None

    latest_file = deals_files[0]
    df = pd.read_csv(latest_file)

    # Ensure numeric columns
    for col in ["current_price", "retail_price", "discount_pct", "deal_rating"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df.sort_values("discount_pct", ascending=False)


def get_store_name(store_id):
    """Convert store ID to store name"""
    store_names = {
        1: "Steam",
        2: "GameBillet",
        3: "Green Man Gaming",
        5: "GOG",
        6: "Epic Games Store",
        7: "Fanatical",
        8: "Microsoft Store",
        10: "Humble Bundle",
        11: "2Game",
        12: "Gamesplanet",
        13: "Voidu",
        14: "Gamer's Gate",
        15: "WinGameStore",
        16: "Allyouplay",
        17: "IndieGala",
        18: "Shopify",
        19: "DreamGame",
        20: "GamersGate",
        21: "Nuuvem",
        22: "Glyph",
        23: "GameStop",
        24: "Oculus",
        25: "Best Buy",
        26: "Nintendo",
        27: "PlayStation Store",
        28: "Ubisoft",
        29: "Bethesda",
        30: "Blizzard",
        31: "Rockstar Games",
        32: "2K Games",
        33: "Borderlands",
        34: "Amazon",
        35: "Twitch",
        36: "Instant Gaming",
        37: "Eneba",
        38: "Kinguin",
        39: "Gamers Gate",
        40: "MacGameStore",
        41: "GamePlanet",
    }
    return store_names.get(int(store_id), f"Store {int(store_id)}")


def format_deal_quality(quality):
    """Format deal quality with color coding"""
    colors = {
        "Exceptional": "🔴",
        "Excellent": "🟡",
        "Good": "🟢",
        "Moderate": "🔵",
        "Minimal": "⚪",
    }
    return f"{colors.get(quality, '')} {quality}"


def page_deals_overview():
    """Main deals overview page"""
    st.title("🎮 PlaySmart Game Deal Tracker")
    st.markdown("Find the best game deals happening right now")

    st.info(
        "💡 **Note:** We're displaying the top 100 best-rated deals from CheapShark API. "
        "There may be additional deals available, but these represent the highest-quality deals across 90+ retailers."
    )

    deals = load_deals_data()

    if deals is None or deals.empty:
        st.warning("No deals data available. Run the pipeline first: `python pipeline/pipeline.py`")
        return

    # Summary metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Deals Available", len(deals))

    with col2:
        avg_discount = deals["discount_pct"].mean() if "discount_pct" in deals.columns else 0
        st.metric("Average Discount", f"{avg_discount:.1f}%")

    with col3:
        max_discount = deals["discount_pct"].max() if "discount_pct" in deals.columns else 0
        st.metric("Best Discount", f"{max_discount:.0f}%")

    st.divider()

    # Top stores and price distribution charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏪 Top Stores by Deal Count")
        if "store_id" in deals.columns:
            store_counts = deals["store_id"].value_counts().head(8)
            store_labels = [get_store_name(int(s)) for s in store_counts.index]
            fig = px.bar(
                x=store_counts.values,
                y=store_labels,
                orientation="h",
                labels={"x": "Number of Deals", "y": "Store"},
                color=store_counts.values,
                color_continuous_scale="Viridis",
                text=store_counts.values
            )
            fig.update_traces(textposition="outside")
            fig.update_layout(height=300, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("💰 Price Range Distribution")
        if "current_price" in deals.columns:
            fig = px.histogram(
                deals,
                x="current_price",
                nbins=15,
                labels={"current_price": "Current Price ($)", "count": "Number of Games"},
                color_discrete_sequence=["#00ff88"]
            )
            fig.update_traces(textposition="outside", texttemplate="%{y}")
            fig.update_layout(height=300, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Top deals table
    st.subheader("🔥 Best Deals Right Now")

    # Filter controls
    col1, col2 = st.columns(2)

    with col1:
        min_discount = st.slider(
            "Minimum Discount %",
            min_value=0,
            max_value=90,
            value=50,
            step=5
        )

    with col2:
        max_price = st.slider(
            "Maximum Price ($)",
            min_value=0,
            max_value=70,
            value=70,
            step=5
        )

    # Apply filters
    filtered_deals = deals[
        (deals["discount_pct"] >= min_discount) &
        (deals["current_price"] <= max_price)
    ]

    # Display deals as table with thumbnails
    if len(filtered_deals) > 0:
        st.info(f"Showing {len(filtered_deals)} deals matching your criteria")

        # Build table data
        table_data = []
        for _, deal in filtered_deals.iterrows():
            thumb_url = deal.get('thumbnail', '')

            table_data.append({
                'Cover': thumb_url if thumb_url and isinstance(thumb_url, str) and thumb_url.startswith('http') else '',
                'Game Title': deal.get('title', 'Unknown'),
                'Current Price': f"${deal.get('current_price', 0):.2f}",
                'Retail Price': f"${deal.get('retail_price', 0):.2f}",
                'Discount %': f"{deal.get('discount_pct', 0):.1f}%",
                'Deal Rating': f"{deal.get('deal_rating', 0):.1f}/10",
                'Store': get_store_name(deal.get('store_id', 0))
            })

        # Display as dataframe with image column
        display_df = pd.DataFrame(table_data)
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                'Cover': st.column_config.ImageColumn(
                    'Cover',
                    width='large',
                    help='Game cover image'
                ),
            }
        )
    else:
        st.warning("No deals match your criteria. Try adjusting the filters.")

    st.divider()

    # Discount distribution chart
    st.subheader("📊 Discount Distribution")
    if "discount_pct" in deals.columns:
        fig = px.histogram(
            deals,
            x="discount_pct",
            nbins=20,
            labels={"discount_pct": "Discount %", "count": "Number of Games"},
            color_discrete_sequence=["#00ff88"]
        )
        fig.update_traces(textposition="outside", texttemplate="%{y}")
        fig.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)


def page_best_deals():
    """Page showing the absolute best deals"""
    st.title("🏆 Best Deals - Ranked")
    st.markdown("Games with the deepest discounts from their retail price")

    deals = load_deals_data()

    if deals is None or deals.empty:
        st.warning("No deals data available")
        return

    # Show top 20 deals
    top_deals = deals.head(20)

    for idx, (_, deal) in enumerate(top_deals.iterrows(), 1):
        with st.container():
            col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])

            with col1:
                st.write(f"**{idx}. {deal.get('title', 'Unknown')}**")
                store_name = get_store_name(deal.get('store_id', 0))
                st.caption(f"📦 {store_name}")

            with col2:
                st.metric(
                    "Current Price",
                    f"${deal.get('current_price', 0):.2f}",
                    delta=f"-{deal.get('discount_pct', 0):.0f}%"
                )

            with col3:
                st.metric("Retail Price", f"${deal.get('retail_price', 0):.2f}")

            with col4:
                st.metric("Deal Rating", f"{deal.get('deal_rating', 0):.2f}")

            with col5:
                quality = deal.get("deal_quality", "Unknown")
                st.write(format_deal_quality(quality))

            st.divider()


def page_store_comparison():
    """Compare deals across stores"""
    st.title("🏪 Store Comparison")
    st.markdown("See which stores have the best deals")

    deals = load_deals_data()

    if deals is None or deals.empty:
        st.warning("No deals data available")
        return

    if "store_id" not in deals.columns:
        st.warning("Store information not available")
        return

    # Get unique store IDs with their counts
    store_counts = deals["store_id"].value_counts()
    store_options = {get_store_name(sid): sid for sid in store_counts.index}
    selected_store_names = st.multiselect(
        "Select stores to compare",
        options=list(store_options.keys()),
        default=list(store_options.keys())[:5] if len(store_options) > 5 else list(store_options.keys())
    )

    selected_store_ids = [store_options[name] for name in selected_store_names]
    filtered = deals[deals["store_id"].isin(selected_store_ids)]

    # Metrics by store
    store_metrics = []
    for store_id in selected_store_ids:
        store_deals = filtered[filtered["store_id"] == store_id]
        store_metrics.append({
            "Store": get_store_name(store_id),
            "Deal Count": len(store_deals),
            "Avg Discount": store_deals["discount_pct"].mean(),
            "Max Discount": store_deals["discount_pct"].max(),
            "Avg Price": store_deals["current_price"].mean(),
        })

    metrics_df = pd.DataFrame(store_metrics)

    st.subheader("Store Metrics")
    st.dataframe(metrics_df, use_container_width=True, hide_index=True)

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Average Discount by Store")
        fig = px.bar(
            metrics_df,
            x="Store",
            y="Avg Discount",
            color="Avg Discount",
            color_continuous_scale="Viridis",
            text="Avg Discount"
        )
        fig.update_traces(textposition="outside", texttemplate="%{y:.1f}%")
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Deal Count by Store")
        fig = px.bar(
            metrics_df,
            x="Store",
            y="Deal Count",
            color="Deal Count",
            color_continuous_scale="Blues",
            text="Deal Count"
        )
        fig.update_traces(textposition="outside", texttemplate="%{y}")
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)


def main():
    """Main app navigation"""
    st.sidebar.title("🎮 PlaySmart")
    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "Navigation",
        ["🔥 Active Deals", "🏆 Best Deals", "🏪 Store Comparison"],
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("**About PlaySmart**")
    st.sidebar.info(
        "Track game prices and find the best deals across multiple stores. "
        "Updated regularly with the latest game price drops and sales."
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Last Updated**")
    data_dir = Path(__file__).parent.parent / "processed_data"
    deals_files = list(data_dir.glob("deals_processed*.csv"))
    if deals_files:
        latest_file = max(deals_files, key=lambda p: p.stat().st_mtime)
        mtime = datetime.fromtimestamp(latest_file.stat().st_mtime)
        st.sidebar.caption(f"{mtime.strftime('%Y-%m-%d %H:%M:%S')}")

    # Route to pages
    if page == "🔥 Active Deals":
        page_deals_overview()
    elif page == "🏆 Best Deals":
        page_best_deals()
    elif page == "🏪 Store Comparison":
        page_store_comparison()


if __name__ == "__main__":
    main()
