import sqlite3
import os

# Ensure the database file is in the same folder as this script
db_path = os.path.join(os.path.dirname(__file__), "services.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    location TEXT,
    phone TEXT,
    whatsapp TEXT,
    latitude REAL,
    longitude REAL,
    rating REAL
)
""")

# Clear old data
cursor.execute("DELETE FROM services")

# Insert sample rich dataset
data = [
    ("Mulago Hospital", "hospital", "Kampala", "+256700000001", "+256700000001", 0.3476, 32.5825, 4.5),
    ("Speke Hotel", "hotel", "Kampala", "+256700000003", "+256700000003", 0.3136, 32.5811, 4.3),
    ("Shell Ntinda", "petrol station", "Kampala", "+256700000004", "+256700000004", 0.3500, 32.6100, 4.0),
    ("Makerere University", "school", "Kampala", "+256700000005", "+256700000005", 0.3333, 32.5700, 4.6),
    ("Stanbic ATM", "atm", "Kampala", "+256700000006", "+256700000006", 0.3200, 32.5800, 4.1),
    ("Kampala Restaurant", "restaurant", "Kampala", "+256700000007", "+256700000007", 0.3100, 32.5750, 4.0),
    ("Mukono General Hospital", "hospital", "Mukono", "+256700000008", "+256700000008", 0.3533, 32.7553, 4.0),
    ("Ridah Hotel", "hotel", "Mukono", "+256700000009", "+256700000009", 0.3600, 32.7600, 4.2),
    ("Kayunga Hospital", "hospital", "Kayunga", "+256700000012", "+256700000012", 0.7025, 32.8886, 3.8),
    ("Kireka Clinic", "hospital", "Kireka", "+256700000015", "+256700000015", 0.3500, 32.6500, 3.7)
]

cursor.executemany("""
INSERT INTO services (name, type, location, phone, whatsapp, latitude, longitude, rating)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", data)

conn.commit()
conn.close()
print("Database created successfully at", db_path)