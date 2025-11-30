from abc import ABC, abstractmethod
from typing import Dict, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseCountyScraper(ABC):
    """
    Abstract base class for county appraisal district scrapers.
    Each Texas county inherits this and implements county-specific logic.

    This modular design allows easy addition of new counties.
    """

    def __init__(self, county_name: str):
        self.county_name = county_name
        self.logger = logger

    @abstractmethod
    def search_by_address(self, address: str) -> Optional[Dict]:
        """
        Search county appraisal district by property address.

        Args:
            address: Full street address

        Returns:
            Dict with assessor data or None if not found
        """
        pass

    @abstractmethod
    def get_base_url(self) -> str:
        """Return the base URL for this county's appraisal district."""
        pass

    def normalize_owner_name(self, owner_name: str) -> str:
        """Common utility to clean owner names."""
        if not owner_name:
            return ""
        return owner_name.strip().upper()

    def parse_value(self, value_str: str) -> float:
        """Common utility to parse dollar values."""
        if not value_str:
            return 0.0

        # Remove $, commas, and convert to float
        cleaned = value_str.replace('$', '').replace(',', '').strip()
        try:
            return float(cleaned)
        except ValueError:
            return 0.0

    def extract_assessor_data(self, raw_data: Dict) -> Dict:
        """
        Template method to standardize assessor data format.
        Override in subclass if needed.
        """
        return {
            'county': self.county_name,
            'parcel_number': raw_data.get('parcel_number'),
            'account_number': raw_data.get('account_number'),
            'owner_name': self.normalize_owner_name(raw_data.get('owner_name')),
            'owner_mailing_address': raw_data.get('owner_mailing_address'),
            'appraised_land_value': self.parse_value(raw_data.get('land_value')),
            'appraised_improvement_value': self.parse_value(raw_data.get('improvement_value')),
            'total_appraised_value': self.parse_value(raw_data.get('total_value')),
            'tax_year': raw_data.get('tax_year')
        }

    def log_search(self, address: str, success: bool):
        """Log search attempts for debugging."""
        status = "SUCCESS" if success else "FAILED"
        self.logger.info(f"[{self.county_name}] {status}: {address}")