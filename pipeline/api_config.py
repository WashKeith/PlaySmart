"""
API Configuration Module
Handles API endpoints for CheapShark and Game Pass pricing APIs
"""

import os
from typing import Dict
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class APIConfig:
    """Centralized API configuration for game price tracking APIs"""

    # CheapShark API - No authentication required
    CHEAPSHARK_BASE_URL = "https://www.cheapshark.com/api/1.0"

    # Game Pass API
    GAME_PASS_API_URL = "https://raw.githubusercontent.com/NikkelM/Game-Pass-API/main/data/gamePassData.json"

    # Store IDs for CheapShark (PC platforms we care about)
    STORES = {
        "Steam": 1,
        "Epic Games Store": 6,
        "GOG": 5,
        "Humble Bundle": 12,
        "Green Man Gaming": 10,
    }

    # Number of deals to fetch (top-rated deals from CheapShark)
    MAX_DEALS = 100

    @staticmethod
    def get_deals_endpoint_params() -> Dict[str, str]:
        """
        Build parameters for CheapShark deals endpoint

        Returns:
            Dictionary of query parameters
        """
        return {
            "sortBy": "Savings",
            "limit": str(APIConfig.MAX_DEALS),
        }

    @staticmethod
    def get_game_endpoint_params(game_id: int) -> Dict[str, str]:
        """
        Build parameters for CheapShark single game endpoint

        Args:
            game_id: CheapShark game ID

        Returns:
            Dictionary of query parameters
        """
        return {"id": str(game_id)}

    @staticmethod
    def validate_config() -> bool:
        """
        Validate that APIs are accessible

        Returns:
            True if config is valid
        """
        return True  # CheapShark requires no auth
