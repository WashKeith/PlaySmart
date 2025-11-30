"""
Master Pipeline Script
Orchestrates the complete data pipeline: fetch -> transform -> save
Run this script to execute the entire end-to-end pipeline with one command
"""

import logging
import os
import sys
from datetime import datetime
import pandas as pd
from pathlib import Path

# Add pipeline directory to path
sys.path.insert(0, os.path.dirname(__file__))

from api_config import APIConfig
from fetch_data import GamePriceFetcher
from transform import GameDataTransformer

# Configure logging
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / f"pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class GameDealPipeline:
    """Master pipeline for fetching, transforming, and saving game deal data"""

    def __init__(self):
        """Initialize pipeline with data directories"""
        self.base_dir = Path(__file__).parent.parent
        self.raw_dir = self.base_dir / "data_raw"
        self.processed_dir = self.base_dir / "data_processed"

        # Create directories if they don't exist
        self.raw_dir.mkdir(exist_ok=True)
        self.processed_dir.mkdir(exist_ok=True)

        logger.info(f"Pipeline initialized")
        logger.info(f"Raw data directory: {self.raw_dir}")
        logger.info(f"Processed data directory: {self.processed_dir}")

    def fetch_deals(self) -> pd.DataFrame:
        """
        Fetch current game deals from CheapShark

        Returns:
            DataFrame with deal information or None if failed
        """
        logger.info("Starting game deals fetch...")
        fetcher = GamePriceFetcher()

        try:
            df = fetcher.fetch_deals()
            if df is not None and len(df) > 0:
                # Save raw data
                raw_file = self.raw_dir / f"deals_raw_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                df.to_csv(raw_file, index=False)
                logger.info(f"Saved raw deals data to {raw_file}")
                return df
            else:
                logger.warning("No deals data retrieved")
                return None
        except Exception as e:
            logger.error(f"Error fetching deals: {e}")
            return None

    def transform_and_save_deals(self, deals_df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform game deal data and save to processed directory

        Args:
            deals_df: Raw game deals DataFrame

        Returns:
            Transformed DataFrame
        """
        logger.info("Starting transformation of deals data...")

        if deals_df is None or deals_df.empty:
            logger.warning("No data to transform")
            return None

        try:
            # Transform data
            transformed = GameDataTransformer.transform_deals_data(deals_df)

            # Sort by deal quality
            transformed = GameDataTransformer.sort_by_deal_quality(transformed)

            # Save processed data
            processed_file = self.processed_dir / f"deals_processed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            transformed.to_csv(processed_file, index=False)
            logger.info(f"Saved processed deals data to {processed_file}")

            return transformed

        except Exception as e:
            logger.error(f"Error transforming deals: {e}")
            return None

    def create_summary_report(self, deals_df: pd.DataFrame) -> None:
        """Create a summary report of the pipeline run"""
        logger.info("Creating summary report...")

        report_file = self.processed_dir / "pipeline_summary.txt"

        try:
            with open(report_file, "w") as f:
                f.write(f"PlaySmart Pipeline Execution Summary\n")
                f.write(f"{'='*60}\n")
                f.write(f"Execution Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"\nRaw Data Directory: {self.raw_dir}\n")
                f.write(f"Processed Data Directory: {self.processed_dir}\n")

                # Data summary
                if deals_df is not None and not deals_df.empty:
                    f.write(f"\nDeals Summary:\n")
                    f.write(f"  Total Deals: {len(deals_df)}\n")

                    if "discount_pct" in deals_df.columns:
                        f.write(f"  Average Discount: {deals_df['discount_pct'].mean():.2f}%\n")
                        f.write(f"  Max Discount: {deals_df['discount_pct'].max():.2f}%\n")

                    if "deal_quality" in deals_df.columns:
                        quality_counts = deals_df["deal_quality"].value_counts()
                        f.write(f"\n  Deal Quality Breakdown:\n")
                        for quality, count in quality_counts.items():
                            f.write(f"    {quality}: {count}\n")

                    if "store" in deals_df.columns:
                        store_counts = deals_df["store"].value_counts()
                        f.write(f"\n  Deals by Store:\n")
                        for store, count in store_counts.head(10).items():
                            f.write(f"    {store}: {count}\n")

                # File counts
                raw_files = list(self.raw_dir.glob("*_raw*.csv"))
                processed_files = list(self.processed_dir.glob("*_processed*.csv"))

                f.write(f"\nData Files:\n")
                f.write(f"  Raw Data Files: {len(raw_files)}\n")
                f.write(f"  Processed Data Files: {len(processed_files)}\n")
                f.write(f"  Log File: {log_file}\n")

            logger.info(f"Summary report saved to {report_file}")

        except Exception as e:
            logger.error(f"Error creating summary report: {e}")

    def run(self) -> bool:
        """
        Execute the complete pipeline

        Returns:
            True if pipeline runs successfully, False otherwise
        """
        logger.info("="*60)
        logger.info("Starting PlaySmart Game Deal Pipeline")
        logger.info("="*60)

        try:
            # Validate configuration
            if not APIConfig.validate_config():
                logger.error("API configuration validation failed")
                return False

            # Fetch deals
            deals_df = self.fetch_deals()
            if deals_df is None:
                logger.error("Failed to fetch deals. Pipeline failed.")
                return False

            # Transform and save
            transformed_df = self.transform_and_save_deals(deals_df)
            if transformed_df is None:
                logger.error("Failed to transform deals. Pipeline failed.")
                return False

            # Create summary report
            self.create_summary_report(transformed_df)

            logger.info("="*60)
            logger.info("PlaySmart Pipeline Completed Successfully!")
            logger.info("="*60)
            logger.info(f"Check {self.processed_dir} for processed data files")
            logger.info(f"Processed {len(transformed_df)} game deals")
            return True

        except Exception as e:
            logger.error(f"Pipeline execution failed: {e}", exc_info=True)
            return False


if __name__ == "__main__":
    pipeline = GameDealPipeline()
    success = pipeline.run()
    sys.exit(0 if success else 1)
