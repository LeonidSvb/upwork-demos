# Rental Scraping + County Appraisal Pipeline - MVP Prototype

## Overview

This is a **modular, production-ready prototype** for scraping rental listings and querying Texas county appraisal districts.

**What's Demonstrated:**
- ✅ Modular county scraper architecture
- ✅ PostgreSQL database schema
- ✅ Address normalization pipeline
- ✅ Clean separation of concerns
- ✅ Easy extensibility for new counties

## Project Structure

```
rental-scraper-mvp/
├── schema.sql              # PostgreSQL database schema
├── base_county.py          # Abstract base class for county scrapers
├── travis_county.py        # Travis County (Austin) implementation
├── harris_county.py        # Harris County (Houston) implementation
├── address_utils.py        # Address normalization utilities
├── scraper_demo.py         # Complete pipeline demonstration
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Quick Start

### 1. Database Setup

```bash
# Create PostgreSQL database
createdb rental_scraper

# Load schema
psql rental_scraper < schema.sql
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Demo

```bash
python scraper_demo.py
```

## How It Works

### Pipeline Flow

```
Rent.com Scraper → Address Normalizer → County Detector → County Scraper → Database
```

### 1. Rent.com Scraper (Simulated)
- In production: Uses Playwright for JavaScript-heavy pages
- Extracts: address, price, beds, baths, URL
- Handles pagination and dynamic loading

### 2. Address Normalization
```python
from address_utils import normalize_address

result = normalize_address("123 Main St, Austin, TX 78701")
# Returns: {
#   'street_address': '123 Main St',
#   'city': 'Austin',
#   'state': 'TX',
#   'zip_code': '78701'
# }
```

### 3. County Detection
```python
from address_utils import detect_county

county = detect_county('Austin', 'TX')  # Returns: 'Travis'
```

### 4. County Appraisal Scraping

**Modular Design:**
Each county inherits from `BaseCountyScraper` and implements:
- `search_by_address()` - County-specific search logic
- `get_base_url()` - CAD website URL
- Custom parsing for that county's HTML structure

**Example - Adding New County:**

```python
from base_county import BaseCountyScraper

class BexarCountyScraper(BaseCountyScraper):
    def __init__(self):
        super().__init__("Bexar")

    def get_base_url(self):
        return "https://bexar.trueprodigy.com/property-search"

    def search_by_address(self, address):
        # Bexar-specific implementation
        pass
```

## Database Schema

### Tables

**properties**
- Normalized property addresses
- Geocoded lat/lng
- County identification

**rent_listings**
- Scraped rental data
- Links to properties
- Price, beds, baths

**assessor_records**
- Owner information
- Appraised values
- Tax year data

### Relationships
```sql
properties (1) ←→ (many) rent_listings
properties (1) ←→ (many) assessor_records
```

## Production Roadmap

### Phase 1: Core Scraping ✓
- [x] Modular county structure
- [x] Database schema
- [x] Address normalization
- [ ] Real Playwright implementation for rent.com
- [ ] Anti-bot measures (user agents, delays, proxies)

### Phase 2: Automation
- [ ] Cron job setup
- [ ] Error handling and retries
- [ ] Logging system
- [ ] Rate limiting

### Phase 3: Scale
- [ ] Async scraping (1,000+ properties)
- [ ] Queue system (Celery/RabbitMQ)
- [ ] Monitoring and alerts

## Adding New Counties

1. Create new file: `{county_name}_county.py`
2. Inherit from `BaseCountyScraper`
3. Implement required methods:
   - `get_base_url()`
   - `search_by_address()`
4. Add to factory in `scraper_demo.py`:

```python
scrapers = {
    'Travis': TravisCountyScraper(),
    'Harris': HarrisCountyScraper(),
    'Bexar': BexarCountyScraper(),  # ← Add here
}
```

## Technical Notes

### Why Modular?
Each Texas county has:
- Different website structure
- Different form parameters
- Different HTML parsing requirements
- Different anti-bot protections

Modular design isolates these differences and makes maintenance easy.

### Anti-Bot Strategies
- Random delays between requests
- Rotating user agents
- Proxy rotation (if needed)
- Respect robots.txt
- Session management

### Database Upserts
Schema uses `UNIQUE` constraints and PostgreSQL `ON CONFLICT` for safe upserts:

```python
INSERT INTO properties (full_address, city, state, ...)
VALUES (%s, %s, %s, ...)
ON CONFLICT (full_address) DO UPDATE SET
    updated_at = CURRENT_TIMESTAMP;
```

## Limitations (MVP)

1. **Mock Scraping Data** - Demo uses simulated results
2. **Limited Counties** - Only Travis and Harris implemented
3. **No Geocoding API** - County detection is simplified
4. **No Cron Jobs** - Manual execution only
5. **No Error Recovery** - Production needs retry logic

## Next Steps for Production

1. **Implement real Playwright scraper** for rent.com
2. **Add geocoding API** (Google Maps or Nominatim)
3. **Expand county coverage** (Bexar, Dallas, Tarrant, etc.)
4. **Set up cron jobs** for automated runs
5. **Add monitoring** (Sentry, logging dashboard)
6. **Scale testing** with 1,000+ properties

## Contact

This prototype demonstrates:
- Clean modular architecture
- Production-ready database design
- Extensible county scraping system
- Understanding of Texas CAD websites

Ready to expand into full production system.