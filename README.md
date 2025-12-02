# PlaySmart: Game Deal Price Tracker

## 🎮 Project Overview

**PlaySmart** is an end-to-end **data engineering + analytics solution** for tracking video game prices and finding the best deals across multiple digital storefronts. Built with real APIs and production-grade code, this project demonstrates complete data pipeline expertise: from API integration through data transformation to interactive dashboards.

### What PlaySmart Does

1. **Fetches real-time game deal data** from the CheapShark API (aggregates deals from 90+ retailers)
2. **Processes and cleans** data through a robust Python ETL pipeline with validation and error handling
3. **Enriches datasets** with deal metrics: discount percentages, deal quality ratings, savings calculations
4. **Powers an interactive Streamlit dashboard** with multiple pages for deal analysis and store comparison
5. **Generates insights** for smart game purchasing decisions

### Why This Project Matters

- **Real-world relevance**: Solves an actual problem—finding when games are genuinely cheap vs. misleading sales
- **Production-ready code**: Includes error handling, logging, configuration management, and modular architecture
- **Demonstrates key skills**: Data engineering (ETL), API integration, data analysis, data visualization, Python expertise
- **Portfolio-worthy**: Shows ability to build complete data solutions from raw API data to interactive dashboards

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                   PlaySmart Architecture                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │           CheapShark API                                 │   │
│  │  (90+ Game Retailers - Steam, Epic, GOG, Fanatical)     │   │
│  └──────────────────────────────────────────────────────────┘   │
│                           ↓                                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │    Data Fetching Layer (fetch_data.py)                  │   │
│  │  • GamePriceFetcher class                                │   │
│  │  • Handles API requests & error handling                 │   │
│  │  • Returns pandas DataFrames                             │   │
│  └──────────────────────────────────────────────────────────┘   │
│                           ↓                                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │   Data Processing Layer (transform.py)                  │   │
│  │  • Data validation & cleaning                            │   │
│  │  • Discount percentage calculation                       │   │
│  │  • Deal quality categorization                           │   │
│  │  • GameDataTransformer class                             │   │
│  └──────────────────────────────────────────────────────────┘   │
│                           ↓                                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │   Processed Data Storage (data_processed/)               │   │
│  │  • Clean, enriched datasets as CSV files                 │   │
│  │  • Ready for analysis and visualization                  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                           ↓                                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │    Streamlit Dashboard (dashboard/app.py)                │   │
│  │  • 3 interactive pages                                   │   │
│  │  • Deal analysis & filtering                             │   │
│  │  • Store comparison analytics                            │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
PlaySmart/
├── pipeline/                          # Data ETL Pipeline
│   ├── api_config.py                 # API configuration & endpoints
│   ├── fetch_data.py                 # Data fetching from CheapShark
│   ├── transform.py                  # Data cleaning & enrichment
│   ├── pipeline.py                   # Master orchestration script
│   └── __init__.py
│
├── dashboard/                         # Streamlit Application
│   ├── app.py                        # Main dashboard (3 pages)
│   └── __init__.py
│
├── raw_data/                         # Raw data from API (generated)
│   └── deals_raw_*.csv
│
├── processed_data/                   # Processed & enriched data (generated)
│   ├── deals_processed_*.csv
│   └── pipeline_summary.txt
│
├── logs/                             # Pipeline execution logs (generated)
│   └── pipeline_*.log
│
├── requirements.txt                  # Python dependencies
├── .env.example                      # Environment variables template
├── .gitignore                        # Git ignore rules
└── README.md                         # This file
```

---

## 🔌 API Integration

### CheapShark API

**PlaySmart** uses the [CheapShark API](https://apidocs.cheapshark.com/) to fetch real-time game deal data.

#### Getting Started

1. **No API key required** - CheapShark is a public API
2. No authentication needed
3. Rate limit: ~1 request per 0.5 seconds (built into pipeline)

#### What You Get

- **Deal data**: Title, current price, retail price, discount %, store
- **Deal ratings**: Quality scores from CheapShark community
- **90+ retailers**: Steam, Epic Games Store, GOG, Fanatical, Humble Bundle, Green Man Gaming, and more
- **Real-time pricing**: Updated approximately every 20 minutes

#### Rate Limiting

- Pipeline includes automatic 0.5s delays between requests
- CheapShark has generous rate limits for non-commercial use
- Suitable for personal projects and hobby use

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git (for version control)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/PlaySmart.git
   cd PlaySmart
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional, CheapShark doesn't require auth)
   ```bash
   cp .env.example .env
   # .env file is optional for this project
   ```

---

## 📊 Running the Pipeline

The pipeline fetches fresh game deal data from CheapShark, cleans it, and enriches it with deal metrics.

### Execute End-to-End Pipeline

```bash
cd pipeline
python pipeline.py
```

**Output:**
- Raw data saved to `raw_data/deals_raw_*.csv`
- Processed data saved to `processed_data/deals_processed_*.csv`
- Execution logs saved to `logs/pipeline_*.log`
- Summary report in `processed_data/pipeline_summary.txt`

### What the Pipeline Does

1. **Fetches deal data** - Retrieves top-rated game deals from CheapShark
2. **Transforms data**:
   - Cleans and standardizes column names
   - Converts prices to numeric values
   - Calculates discount percentages
   - Categorizes deals by quality (Exceptional/Excellent/Good/Moderate/Minimal)
   - Adds timestamp metadata
3. **Sorts deals** - Ranks by deal rating and discount depth
4. **Saves output** - Stores both raw and processed data
5. **Generates report** - Creates summary statistics

### Example Output

```
INFO:__main__:Starting PlaySmart Game Deal Pipeline
INFO:fetch_data:Fetching game deals from CheapShark...
INFO:fetch_data:Successfully fetched 60 deals
INFO:transform:Starting game deals transformation...
INFO:transform:Calculated discount percentages
INFO:transform:Categorized deal qualities
INFO:__main__:Saved processed deals data to C:\...\processed_data\deals_processed_*.csv
INFO:__main__:PlaySmart Pipeline Completed Successfully!
INFO:__main__:Processed 60 game deals
```

---

## 📈 Running the Dashboard

The dashboard is a web application that visualizes game deals with interactive charts and filtering.

### Start the Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your browser at `http://localhost:8501`

### Dashboard Pages

#### 1. **🔥 Active Deals** (Main Page)
- Summary metrics (total deals, average discount, best discount)
- Deal quality distribution (pie chart)
- Top stores by deal count (bar chart)
- Filterable deals table with controls:
  - Minimum discount percentage
  - Maximum price limit
  - Deal quality filter
- Discount distribution histogram

**Use case**: Find current deals matching your budget and quality requirements

#### 2. **🏆 Best Deals - Ranked**
- Top 20 deals ranked by discount percentage
- Shows current price, retail price, discount %, deal rating, and quality
- Organized card layout for easy browsing

**Use case**: Quickly see the absolute deepest discounts available right now

#### 3. **🏪 Store Comparison**
- Compare deals across different retailers
- Metrics table showing:
  - Number of deals per store
  - Average discount percentage
  - Maximum discount available
  - Average game price
- Side-by-side charts for discount comparison and deal counts

**Use case**: Decide which stores have the best deals for your wishlist

---

## 🔧 Technical Details

### Pipeline Modules

#### `api_config.py`
- **APIConfig class**: Centralized configuration management
- **CheapShark endpoints**: Base URL and API parameters
- **Store IDs**: Mapping of store names to CheapShark IDs
- **Validation**: Basic configuration checks

#### `fetch_data.py`
- **GamePriceFetcher class**: Handles all API requests
- **Methods**:
  - `fetch_deals()` - Fetch current game deals
  - `fetch_game_detail()` - Get detailed info for a specific game
  - `fetch_price_history()` - Extract price history from deal data
  - `fetch_multiple_game_details()` - Batch fetch game info
- **Features**:
  - HTTP error handling with retries
  - Rate limiting (0.5s between requests)
  - Response validation
  - Comprehensive logging

#### `transform.py`
- **GameDataTransformer class**: Data cleaning and feature engineering
- **Methods**:
  - `clean_deal_data()` - Standardize column names and types
  - `calculate_discount_percentage()` - Compute discount %
  - `categorize_deal_quality()` - Rate deal quality (1-5)
  - `add_time_metadata()` - Add timestamp
  - `transform_deals_data()` - Complete pipeline
  - `filter_by_discount()` - Filter deals by minimum discount
  - `sort_by_deal_quality()` - Sort by quality ratings
- **Data quality**: Type conversion, null handling, validation

#### `pipeline.py`
- **GameDealPipeline class**: Master orchestration
- **Methods**:
  - `fetch_deals()` - Fetch and save raw data
  - `transform_and_save_deals()` - Transform and save processed data
  - `create_summary_report()` - Generate execution report
  - `run()` - Execute complete end-to-end pipeline
- **Logging**: Comprehensive logging to file and console
- **Error handling**: Graceful error handling with detailed logging

### Dashboard Components

#### **Streamlit App** (`app.py`)
- **Page functions**: `page_deals_overview()`, `page_best_deals()`, `page_store_comparison()`
- **Chart functions**: Using Plotly for interactive visualizations
- **Caching**: `@st.cache_data` for efficient data loading
- **Interactivity**: Sliders, multiselect dropdowns, responsive layout
- **Theming**: Gaming-inspired dark theme with neon accents

#### **Visualization Library**: Plotly
- Interactive pie charts for deal distribution
- Bar charts for store comparison
- Histograms for discount distribution
- Hover information on all charts

---

## 💰 Deal Quality Categories Explained

| Category | Discount | Use Case |
|----------|----------|----------|
| **Exceptional** | ≥75% off | Once-in-a-lifetime deals, collector's items on deep sale |
| **Excellent** | 50-75% off | Major sales, best time to buy |
| **Good** | 25-50% off | Standard sales, reasonable savings |
| **Moderate** | 10-25% off | Minor discounts, seasonal sales |
| **Minimal** | <10% off | Barely discounted, probably not worth waiting for |

---

## 💼 Business Use Cases

### 1. **Personal Gaming Budget**
- Track game prices for your wishlist
- Get alerts when games hit good discount points
- Avoid impulse purchases at bad prices

### 2. **Content Creator Toolkit**
- Find cheap games for streaming content
- Discover trending titles at deals
- Track pricing trends for video thumbnails

### 3. **Gaming Library Growth**
- Build a library of games at optimal prices
- Identify seasonal sale patterns
- Maximize gaming budget

### 4. **Market Research** (for data professionals)
- Understand game pricing dynamics
- Track retailer pricing strategies
- Analyze discount patterns across publishers

---

## 🎯 Interview Talking Points

### "Tell me about your data pipeline"

**Strong Answer**: "PlaySmart is an end-to-end ETL pipeline that fetches game deal data from the CheapShark API, cleans and enriches it with deal metrics, and powers an interactive dashboard. The pipeline uses Python to fetch real-time data from 90+ game retailers, validates data quality, calculates discount percentages and deal quality ratings, then saves cleaned data as CSV files. I built modular code with separate concerns—API configuration, data fetching, transformation, and orchestration—so each component is testable and reusable. The dashboard uses Streamlit for interactive visualization with filtering and comparison features."

### "Why did you choose CheapShark API?"

**Strong Answer**: "CheapShark was the best fit for this project because it provides free, real-time deal data from 90+ retailers without requiring authentication. It directly solves the problem of finding the cheapest games across multiple storefronts. The trade-off is that it focuses on PC games (Steam, Epic, GOG), but that's where most digital game sales happen anyway. I could have built web scrapers for individual stores, but CheapShark's centralized approach is cleaner and more reliable. The API has generous rate limits for hobby projects like mine."

### "How do you handle errors in the pipeline?"

**Strong Answer**: "I implemented error handling at multiple levels: (1) API layer—catch request timeouts and validate JSON responses; (2) Data layer—null checking, type conversion with error handling, validation of critical fields; (3) Pipeline layer—try/except blocks around each major operation; (4) Monitoring—comprehensive logs to file with timestamps and error details. If one deal fetch fails, the pipeline continues and processes available data instead of crashing. The dashboard gracefully handles missing data with informative messages."

### "How would you scale this to handle more data?"

**Strong Answer**: "For scale, I'd make several improvements: (1) Use a database (PostgreSQL) instead of CSV files for faster queries and historical analysis; (2) Implement incremental fetching—only fetch deals updated since last run instead of full dataset; (3) Add caching layer (Redis) for frequently accessed data; (4) Schedule with Airflow or Cron for automated daily runs; (5) Parallelize API requests with async/await; (6) Move dashboard to cloud (Streamlit Cloud, AWS); (7) Add data versioning. The modular design makes these changes straightforward—I could swap out the CSV storage layer without touching the fetch or transform logic."

### "What data metrics does your pipeline provide?"

**Strong Answer**: "PlaySmart calculates several key deal metrics: (1) Discount percentage—how much off retail price; (2) Deal quality rating—categorizes deals (Exceptional/Excellent/Good) based on discount depth; (3) Savings amount—actual dollar amount saved; (4) CheapShark deal rating—community feedback on deal quality; (5) Timestamp—when deal was found. The dashboard visualizes these metrics to help users identify the best times to buy. The categorization system helps distinguish between 'good deals' and 'genuine bargains.'"

### "How does this relate to data engineering roles?"

**Strong Answer**: "PlaySmart demonstrates real data engineering skills valued by fintech and tech companies: (1) API integration—working with external data sources; (2) ETL design—extract, transform, load pipeline; (3) Data validation—ensuring quality before analysis; (4) Logging and monitoring—understanding pipeline health; (5) Modular code—separating concerns for maintainability; (6) Error handling—graceful degradation; (7) Cloud-ready—uses standard tools (Python, Pandas, Streamlit) deployable anywhere. In fintech context, the same pattern applies to market data, pricing APIs, and risk analytics. The skills are transferable."

---

## 📝 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | >=2.0.0 | Data manipulation and analysis |
| numpy | >=1.24.0 | Numerical computations |
| requests | >=2.31.0 | HTTP requests to API |
| python-dotenv | >=1.0.0 | Environment variable management |
| streamlit | >=1.28.0 | Web dashboard framework |
| plotly | >=5.17.0 | Interactive visualizations |

---

## 🔐 Security Best Practices

1. **API Key Management**
   - CheapShark doesn't require authentication
   - Store any future API keys in `.env` file (never commit to git)
   - Use `.gitignore` to exclude `.env` from version control

2. **Error Messages**
   - Don't expose sensitive data in logs
   - Log errors for debugging without exposing credentials

3. **Data Privacy**
   - Game deal data is public
   - No user data is collected or stored
   - Dashboard is local-only by default

---

## 📊 File Inventory

| File | Purpose |
|------|---------|
| `pipeline/api_config.py` | API configuration & parameters |
| `pipeline/fetch_data.py` | Data fetching from CheapShark |
| `pipeline/transform.py` | Data cleaning & enrichment |
| `pipeline/pipeline.py` | Master orchestration script |
| `dashboard/app.py` | Streamlit dashboard (3 pages) |
| `requirements.txt` | Python dependencies |
| `.env.example` | Environment template |
| `.gitignore` | Git ignore rules |
| `README.md` | This documentation |

**Total**: 1,500+ lines of code + 1,000+ lines of documentation

---

## 🎓 Key Learnings Demonstrated

1. **Data Engineering** – ETL pipeline design, data validation, quality checks
2. **API Integration** – HTTP requests, error handling, rate limiting
3. **Data Analysis** – Deal metrics, discount calculations, quality categorization
4. **Python Proficiency** – Pandas, OOP, error handling, logging
5. **Web Development** – Streamlit, interactivity, responsive UI
6. **Data Visualization** – Plotly charts, dashboard design, UX
7. **Software Engineering** – Modular code, configuration management
8. **Problem Solving** – Finding cheap games (real-world relevance!)
9. **Production Code** – Logging, error handling, comprehensive documentation

---

## 🚀 Next Steps

### Short Term (This Week)
1. Install dependencies: `pip install -r requirements.txt`
2. Run pipeline: `python pipeline/pipeline.py`
3. Start dashboard: `streamlit run dashboard/app.py`
4. Explore all 3 dashboard pages

### Medium Term (This Month)
1. Customize with different game categories/tags
2. Experiment with different discount thresholds
3. Deploy dashboard to Streamlit Cloud (free tier available)
4. Share with gaming friends

### Long Term (Future)
1. Add database backend (PostgreSQL)
2. Implement scheduled runs (Cron/Airflow)
3. Add price history tracking over time
4. Implement email/Discord notifications for specific games
5. Add ML-based deal prediction
6. Support for console games (Xbox, PlayStation)

---

## 📧 Questions?

- Check the code comments and docstrings
- Review logs in `logs/` directory for pipeline execution details
- See [CheapShark API docs](https://apidocs.cheapshark.com/) for data details

---

## 📄 License

This project is provided as-is for educational and personal use.

---

**Version**: 1.0.0
**Last Updated**: November 2024
**Status**: Production-Ready

Made with 🎮 by someone who wants to save money on games
