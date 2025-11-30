"""
Data Fetching Module
Fetches game price data from CheapShark API and Game Pass API
"""

import requests
import pandas as pd
import logging
import time
from typing import Optional, List
from api_config import APIConfig

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GamePriceFetcher:
    """Fetches game price data from CheapShark and Game Pass APIs"""

    def __init__(self):
        """Initialize fetcher with rate limiting"""
        self.cheapshark_url = APIConfig.CHEAPSHARK_BASE_URL
        self.rate_limit_delay = 0.5  # seconds between requests
        self.timeout = 10  # seconds

    def fetch_deals(self) -> Optional[pd.DataFrame]:
        """
        Fetch current game deals from CheapShark

        Returns:
            DataFrame with deal information or None if failed
        """
        try:
            logger.info("Fetching game deals from CheapShark...")
            url = f"{self.cheapshark_url}/deals"
            params = APIConfig.get_deals_endpoint_params()

            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()

            deals = response.json()
            if not deals:
                logger.warning("No deals returned from API")
                return None

            # Convert to DataFrame
            df = pd.DataFrame(deals)
            logger.info(f"Successfully fetched {len(df)} deals")
            return df

        except requests.RequestException as e:
            logger.error(f"Error fetching deals: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error fetching deals: {e}")
            return None

    def fetch_game_detail(self, game_id: str) -> Optional[dict]:
        """
        Fetch detailed information for a specific game including price history

        Args:
            game_id: CheapShark game ID

        Returns:
            Dictionary with game details or None if failed
        """
        try:
            time.sleep(self.rate_limit_delay)  # Rate limiting

            url = f"{self.cheapshark_url}/games"
            params = APIConfig.get_game_endpoint_params(int(game_id))

            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()

            game_data = response.json()
            return game_data

        except requests.RequestException as e:
            logger.error(f"Error fetching game {game_id}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error fetching game {game_id}: {e}")
            return None

    def fetch_price_history(self, game_id: str) -> Optional[pd.DataFrame]:
        """
        Fetch price history for a specific game

        Args:
            game_id: CheapShark game ID

        Returns:
            DataFrame with price history or None if failed
        """
        try:
            game_data = self.fetch_game_detail(game_id)
            if not game_data or "deals" not in game_data:
                return None

            deals = game_data.get("deals", [])
            if not deals:
                return None

            # Extract price history from deals
            history_list = []
            for deal in deals:
                history_list.append({
                    "store": deal.get("storeName"),
                    "price": deal.get("price"),
                    "retail_price": deal.get("retailPrice"),
                    "discount": deal.get("savings"),
                    "deal_rating": deal.get("dealRating"),
                })

            if history_list:
                return pd.DataFrame(history_list)
            return None

        except Exception as e:
            logger.error(f"Error fetching price history for game {game_id}: {e}")
            return None

    def fetch_multiple_game_details(self, game_ids: List[str]) -> pd.DataFrame:
        """
        Fetch detailed information for multiple games

        Args:
            game_ids: List of CheapShark game IDs

        Returns:
            DataFrame with game details
        """
        results = []

        for i, game_id in enumerate(game_ids):
            logger.info(f"Fetching details for game {i+1}/{len(game_ids)} (ID: {game_id})...")
            game_data = self.fetch_game_detail(game_id)

            if game_data:
                # Extract key information
                processed = {
                    "game_id": game_id,
                    "title": game_data.get("info", {}).get("title", "Unknown"),
                    "thumb": game_data.get("info", {}).get("thumb", ""),
                    "current_price": game_data.get("deals", [{}])[0].get("price") if game_data.get("deals") else None,
                    "retail_price": game_data.get("deals", [{}])[0].get("retailPrice") if game_data.get("deals") else None,
                    "discount_percent": game_data.get("deals", [{}])[0].get("savings") if game_data.get("deals") else None,
                    "deal_rating": game_data.get("deals", [{}])[0].get("dealRating") if game_data.get("deals") else None,
                    "store_id": game_data.get("deals", [{}])[0].get("storeID") if game_data.get("deals") else None,
                }
                results.append(processed)

        return pd.DataFrame(results) if results else pd.DataFrame()
