"""
FinSight Data Pipeline Package

A production-ready ETL pipeline for financial market data.

Modules:
- api_config: API configuration and parameter management
- fetch_data: Data fetching from Alpha Vantage API
- transform: Data cleaning and feature engineering
- pipeline: Master orchestration script
"""

__version__ = "1.0.0"
__author__ = "Data Engineer"
__description__ = "FinSight: Finance Market Analytics Dashboard"

from .api_config import APIConfig
from .fetch_data import DataFetcher
from .transform import DataTransformer
from .pipeline import DataPipeline

__all__ = ["APIConfig", "DataFetcher", "DataTransformer", "DataPipeline"]
