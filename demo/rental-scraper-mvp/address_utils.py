import re
from typing import Dict, Optional


def normalize_address(raw_address: str) -> Dict[str, str]:
    """
    Normalize and split address into components.

    Args:
        raw_address: Full address string from rental listing

    Returns:
        Dict with street_address, city, state, zip_code

    Example:
        "123 Main St Apt 4B, Austin, TX 78701"
        -> {
            'street_address': '123 Main St Apt 4B',
            'city': 'Austin',
            'state': 'TX',
            'zip_code': '78701'
        }
    """

    # Remove extra whitespace
    address = ' '.join(raw_address.split())

    # Extract ZIP code (5 or 9 digits)
    zip_match = re.search(r'\b(\d{5}(?:-\d{4})?)\b', address)
    zip_code = zip_match.group(1) if zip_match else None

    # Extract state (2 letter code before ZIP)
    state_match = re.search(r'\b([A-Z]{2})\b', address)
    state = state_match.group(1) if state_match else None

    # Split by comma for city extraction
    parts = [p.strip() for p in address.split(',')]

    street_address = parts[0] if len(parts) > 0 else ''
    city = parts[1] if len(parts) > 1 else ''

    # Clean up city (remove state and zip if present)
    if city and state:
        city = city.replace(state, '').strip()
    if city and zip_code:
        city = city.replace(zip_code, '').strip()

    return {
        'full_address': raw_address,
        'street_address': street_address,
        'city': city,
        'state': state,
        'zip_code': zip_code
    }


def detect_county(city: str, state: str) -> Optional[str]:
    """
    Detect county from city/state.

    In production, use geocoding API (Google Maps, Nominatim)
    This is simplified mapping for Texas cities.
    """

    texas_counties = {
        'Austin': 'Travis',
        'Houston': 'Harris',
        'San Antonio': 'Bexar',
        'Dallas': 'Dallas',
        'Fort Worth': 'Tarrant',
        'El Paso': 'El Paso',
        'Arlington': 'Tarrant',
        'Corpus Christi': 'Nueces',
        'Plano': 'Collin',
        'Laredo': 'Webb'
    }

    if state == 'TX' and city in texas_counties:
        return texas_counties[city]

    # In production: call geocoding API
    return None


def clean_listing_price(price_str: str) -> float:
    """
    Clean rental price string to float.

    Examples:
        "$1,500/mo" -> 1500.0
        "$2000 per month" -> 2000.0
        "1250" -> 1250.0
    """
    if not price_str:
        return 0.0

    # Remove common strings
    cleaned = price_str.replace('/mo', '').replace('per month', '')
    cleaned = cleaned.replace('$', '').replace(',', '').strip()

    try:
        return float(cleaned)
    except ValueError:
        return 0.0