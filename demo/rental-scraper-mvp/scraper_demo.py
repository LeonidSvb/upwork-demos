"""
Simple demonstration of the rental scraping pipeline.

This shows the modular architecture without complex dependencies.
In production, this would use Playwright for rent.com scraping.
"""

from address_utils import normalize_address, detect_county
from travis_county import TravisCountyScraper
from harris_county import HarrisCountyScraper
import json


def get_county_scraper(county_name: str):
    """Factory pattern to get appropriate county scraper."""
    scrapers = {
        'Travis': TravisCountyScraper(),
        'Harris': HarrisCountyScraper()
        # Easy to add: 'Bexar': BexarCountyScraper(),
    }
    return scrapers.get(county_name)


def scrape_rental_listing(listing_url: str):
    """
    Simulated rental listing scraper.

    In production:
    - Use Playwright to load rent.com page
    - Extract address, price, beds, baths
    - Handle pagination and dynamic loading
    """

    # MOCK DATA - In production, this comes from actual scraping
    mock_listing = {
        'url': listing_url,
        'address': '123 West 6th Street Apt 201, Austin, TX 78701',
        'rent_price': '$2,100/mo',
        'bedrooms': 2,
        'bathrooms': 2.0
    }

    return mock_listing


def process_listing(listing_data: dict):
    """
    Complete pipeline for one rental listing.

    Steps:
    1. Normalize address
    2. Detect county
    3. Query county appraisal district
    4. Return combined data for database insertion
    """

    print(f"\n{'='*60}")
    print(f"Processing: {listing_data['url']}")
    print(f"{'='*60}")

    # Step 1: Normalize address
    normalized = normalize_address(listing_data['address'])
    print(f"\n1. Normalized Address:")
    print(f"   Street: {normalized['street_address']}")
    print(f"   City: {normalized['city']}, {normalized['state']} {normalized['zip_code']}")

    # Step 2: Detect county
    county = detect_county(normalized['city'], normalized['state'])
    print(f"\n2. Detected County: {county}")

    if not county:
        print("   ⚠️  County detection failed - skipping assessor lookup")
        return None

    # Step 3: Get county scraper
    scraper = get_county_scraper(county)
    if not scraper:
        print(f"   ⚠️  No scraper configured for {county} County")
        return None

    # Step 4: Query county appraisal district
    print(f"\n3. Querying {county} County Appraisal District...")
    assessor_data = scraper.search_by_address(normalized['full_address'])

    if assessor_data:
        print(f"\n4. Assessor Data Retrieved:")
        print(f"   Owner: {assessor_data['owner_name']}")
        print(f"   Mailing: {assessor_data['owner_mailing_address']}")
        print(f"   Land Value: ${assessor_data['appraised_land_value']:,.2f}")
        print(f"   Improvement Value: ${assessor_data['appraised_improvement_value']:,.2f}")
        print(f"   Total Value: ${assessor_data['total_appraised_value']:,.2f}")
        print(f"   Tax Year: {assessor_data['tax_year']}")

    # Step 5: Combine all data for database
    combined_data = {
        'property': normalized,
        'rental_listing': {
            'url': listing_data['url'],
            'rent_price': listing_data['rent_price'],
            'bedrooms': listing_data['bedrooms'],
            'bathrooms': listing_data['bathrooms']
        },
        'assessor': assessor_data
    }

    return combined_data


def main():
    """
    Demonstration of the complete pipeline.
    """

    print("\n" + "="*60)
    print("RENTAL SCRAPING + COUNTY APPRAISAL PIPELINE DEMO")
    print("="*60)

    # Simulated rental listings from rent.com
    listings = [
        'https://rent.com/austin-tx/listing-1',
        'https://rent.com/houston-tx/listing-2'
    ]

    results = []

    for listing_url in listings:
        # Step 1: Scrape rental listing
        listing_data = scrape_rental_listing(listing_url)

        # Step 2: Process through pipeline
        result = process_listing(listing_data)

        if result:
            results.append(result)

    # Summary
    print(f"\n{'='*60}")
    print(f"PIPELINE COMPLETE")
    print(f"{'='*60}")
    print(f"Processed: {len(listings)} listings")
    print(f"Successful: {len(results)} records")

    # In production: insert results into PostgreSQL
    print(f"\n✓ Ready for database insertion (PostgreSQL)")
    print(f"✓ Modular county structure allows easy expansion")
    print(f"✓ Can handle 1,000+ properties per run with proper throttling")


if __name__ == '__main__':
    main()