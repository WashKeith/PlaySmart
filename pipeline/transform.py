"""
Data Transformation Module
Cleans, validates, and enriches game price data with deal metrics
"""

import logging
import pandas as pd
import numpy as np
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GameDataTransformer:
    """Handles game deal data cleaning, validation, and feature engineering"""

    @staticmethod
    def clean_deal_data(df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean and standardize game deal data from CheapShark

        Args:
            df: Raw DataFrame from CheapShark API

        Returns:
            Cleaned DataFrame with standardized columns
        """
        logger.info("Cleaning game deal data...")

        df = df.copy()

        # Select and rename key columns
        key_columns = {
            "gameID": "game_id",
            "title": "title",
            "salePrice": "current_price",
            "normalPrice": "retail_price",
            "savings": "discount_amount",
            "dealRating": "deal_rating",
            "storeName": "store",
            "storeID": "store_id",
            "thumb": "thumbnail",
            "isListed": "is_listed",
        }

        # Keep only columns that exist
        available_cols = {k: v for k, v in key_columns.items() if k in df.columns}
        df = df[list(available_cols.keys())].rename(columns=available_cols)

        # Convert price columns to numeric
        price_cols = ["current_price", "retail_price", "discount_amount"]
        for col in price_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # Convert deal rating to numeric
        if "deal_rating" in df.columns:
            df["deal_rating"] = pd.to_numeric(df["deal_rating"], errors="coerce")

        # Remove rows with missing critical data
        df = df.dropna(subset=["game_id", "title", "current_price"])

        logger.info(f"Data cleaning complete. Retained {len(df)} records.")
        return df

    @staticmethod
    def calculate_discount_percentage(df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate discount percentage and savings

        Args:
            df: DataFrame with price data

        Returns:
            DataFrame with added discount columns
        """
        df = df.copy()

        # Calculate discount percentage
        df["discount_pct"] = (
            (df["retail_price"] - df["current_price"]) / df["retail_price"] * 100
        ).round(2)

        # Handle cases where discount_pct might be negative or NaN
        df["discount_pct"] = df["discount_pct"].fillna(0)
        df["discount_pct"] = df["discount_pct"].clip(lower=0)  # No negative discounts

        logger.info("Calculated discount percentages")
        return df

    @staticmethod
    def categorize_deal_quality(df: pd.DataFrame) -> pd.DataFrame:
        """
        Categorize deals based on discount percentage

        Args:
            df: DataFrame with discount_pct column

        Returns:
            DataFrame with added deal_quality column
        """
        df = df.copy()

        def quality(discount):
            if pd.isna(discount):
                return "Unknown"
            elif discount >= 75:
                return "Exceptional"
            elif discount >= 50:
                return "Excellent"
            elif discount >= 25:
                return "Good"
            elif discount >= 10:
                return "Moderate"
            else:
                return "Minimal"

        df["deal_quality"] = df["discount_pct"].apply(quality)
        logger.info("Categorized deal qualities")
        return df

    @staticmethod
    def add_time_metadata(df: pd.DataFrame) -> pd.DataFrame:
        """
        Add time-related metadata for tracking when deals were found

        Args:
            df: DataFrame with deal data

        Returns:
            DataFrame with timestamp column
        """
        df = df.copy()
        df["fetched_at"] = pd.Timestamp.now()
        logger.info("Added timestamp metadata")
        return df

    @staticmethod
    def transform_deals_data(df: pd.DataFrame) -> pd.DataFrame:
        """
        Complete transformation pipeline for game deals

        Args:
            df: Raw game deals DataFrame from CheapShark

        Returns:
            Fully transformed DataFrame with deal metrics
        """
        logger.info("Starting game deals transformation...")

        if df.empty:
            logger.warning("Empty DataFrame provided")
            return df

        # Clean
        df = GameDataTransformer.clean_deal_data(df)

        # Add metrics
        df = GameDataTransformer.calculate_discount_percentage(df)
        df = GameDataTransformer.categorize_deal_quality(df)
        df = GameDataTransformer.add_time_metadata(df)

        # Ensure consistent column order
        base_cols = ["game_id", "title"]
        price_cols = ["retail_price", "current_price", "discount_amount", "discount_pct"]
        rating_cols = ["deal_rating", "deal_quality", "store", "store_id"]
        other_cols = [col for col in df.columns if col not in base_cols + price_cols + rating_cols]

        final_cols = base_cols + price_cols + rating_cols + other_cols
        final_cols = [col for col in final_cols if col in df.columns]

        df = df[final_cols]

        logger.info("Game deals transformation complete")
        return df

    @staticmethod
    def filter_by_discount(df: pd.DataFrame, min_discount_pct: float = 10) -> pd.DataFrame:
        """
        Filter deals to show only those with minimum discount

        Args:
            df: DataFrame with discount_pct column
            min_discount_pct: Minimum discount percentage to include

        Returns:
            Filtered DataFrame
        """
        filtered = df[df["discount_pct"] >= min_discount_pct]
        logger.info(
            f"Filtered to {len(filtered)} deals with >= {min_discount_pct}% discount"
        )
        return filtered

    @staticmethod
    def sort_by_deal_quality(df: pd.DataFrame) -> pd.DataFrame:
        """
        Sort deals by best deal rating and discount percentage

        Args:
            df: DataFrame with deal_rating and discount_pct columns

        Returns:
            Sorted DataFrame
        """
        df = df.copy()
        df = df.sort_values(
            by=["deal_rating", "discount_pct"],
            ascending=[False, False],
            na_position="last"
        )
        logger.info("Sorted deals by quality")
        return df
