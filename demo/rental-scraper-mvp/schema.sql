-- PostgreSQL Schema for Rental Scraping + County Appraisal Pipeline
-- Simple, modular, production-ready structure

CREATE TABLE IF NOT EXISTS properties (
    id SERIAL PRIMARY KEY,
    full_address VARCHAR(500) NOT NULL,
    street_address VARCHAR(300),
    city VARCHAR(100),
    state VARCHAR(2),
    zip_code VARCHAR(10),
    county VARCHAR(100),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(full_address)
);

CREATE INDEX idx_properties_county ON properties(county);
CREATE INDEX idx_properties_zip ON properties(zip_code);

CREATE TABLE IF NOT EXISTS rent_listings (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    listing_url VARCHAR(1000),
    rent_price DECIMAL(10, 2),
    bedrooms INTEGER,
    bathrooms DECIMAL(3, 1),
    listing_source VARCHAR(100) DEFAULT 'rent.com',
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_rent_listings_property ON rent_listings(property_id);
CREATE INDEX idx_rent_listings_active ON rent_listings(is_active);

CREATE TABLE IF NOT EXISTS assessor_records (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    county VARCHAR(100) NOT NULL,
    parcel_number VARCHAR(100),
    account_number VARCHAR(100),
    owner_name VARCHAR(300),
    owner_mailing_address VARCHAR(500),
    appraised_land_value DECIMAL(12, 2),
    appraised_improvement_value DECIMAL(12, 2),
    total_appraised_value DECIMAL(12, 2),
    tax_year INTEGER,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(property_id, tax_year)
);

CREATE INDEX idx_assessor_county ON assessor_records(county);
CREATE INDEX idx_assessor_owner ON assessor_records(owner_name);
CREATE INDEX idx_assessor_year ON assessor_records(tax_year);

-- Update timestamp trigger function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Apply triggers
CREATE TRIGGER update_properties_updated_at BEFORE UPDATE ON properties
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_rent_listings_updated_at BEFORE UPDATE ON rent_listings
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_assessor_records_updated_at BEFORE UPDATE ON assessor_records
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();