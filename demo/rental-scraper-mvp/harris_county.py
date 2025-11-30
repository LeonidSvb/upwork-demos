from base_county import BaseCountyScraper
from typing import Dict, Optional
import time


class HarrisCountyScraper(BaseCountyScraper):
    """
    Harris County (Houston, TX) Appraisal District Scraper

    Production implementation would interact with:
    https://public.hcad.org/records/quicksearch.asp

    Harris County uses a different form structure than Travis,
    demonstrating why modular approach is essential.
    """

    def __init__(self):
        super().__init__("Harris")

    def get_base_url(self) -> str:
        return "https://public.hcad.org/records/quicksearch.asp"

    def search_by_address(self, address: str) -> Optional[Dict]:
        """
        Search Harris County CAD by address.

        Harris County specifics:
        - Uses POST form submission
        - Different field names than Travis
        - Results in different HTML structure
        - May require captcha handling
        """

        self.logger.info(f"Searching Harris County for: {address}")

        # Simulated search delay
        time.sleep(0.5)

        # MOCK DATA - Different structure than Travis County
        mock_result = {
            'account_number': '0123456789',
            'parcel_number': 'HC-12345',
            'owner_name': 'JONES INVESTMENT GROUP',
            'owner_mailing_address': 'PO Box 1234, Houston, TX 77001',
            'land_value': '$200,000',
            'improvement_value': '$450,000',
            'total_value': '$650,000',
            'tax_year': 2024
        }

        self.log_search(address, success=True)

        return self.extract_assessor_data(mock_result)

    def _build_search_payload(self, address: str) -> Dict:
        """
        Build POST payload for Harris County search form.

        Harris uses different parameter names:
        - stnum (street number)
        - stname (street name)
        - owner (owner name - optional)
        """
        parts = address.split(' ', 1)
        street_num = parts[0] if parts else ''
        street_name = parts[1] if len(parts) > 1 else ''

        return {
            'stnum': street_num,
            'stname': street_name,
            'Submit': 'Search'
        }

    def _parse_results_table(self, html: str) -> Dict:
        """
        Parse Harris County specific HTML table structure.

        Their table has different column order than Travis.
        """
        pass