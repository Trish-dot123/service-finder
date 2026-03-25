# db_setup.py
import sqlite3

conn = sqlite3.connect("services.db")
c = conn.cursor()

# Table to store all service centers
c.execute("""
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    service_type TEXT NOT NULL,
    city TEXT NOT NULL,
    phone TEXT,
    latitude REAL,
    longitude REAL
)
""")

# Example data (you can add as many as you want)
c.execute("""
INSERT INTO services (name, service_type, city, phone, latitude, longitude)
VALUES
('Mulago Hospital', 'Hospital', 'Kampala', '0412345678', 0.3386, 32.5825),
('Kampala Serena Hotel', 'Hotel', 'Kampala', '0412341234', 0.3186, 32.5850),
('Cafe Javas', 'Restaurant', 'Kampala', '0412354321', 0.3220, 32.5740)
""")

conn.commit()
conn.close()
print("Database setup complete!")