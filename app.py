from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Search endpoint
@app.route("/search")
def search():
    location = request.args.get("location", "").strip()
    service = request.args.get("service", "").strip()

    if not location or not service:
        return jsonify([])

    conn = sqlite3.connect("services.db")
    c = conn.cursor()

    c.execute("""
        SELECT name, service_type, city, phone, latitude, longitude
        FROM services
        WHERE LOWER(city)=? AND LOWER(service_type)=?
    """, (location.lower(), service.lower()))

    rows = c.fetchall()
    conn.close()

    results = []
    for row in rows:
        results.append({
            "name": row[0],
            "service_type": row[1],
            "city": row[2],
            "phone": row[3],
            "lat": row[4],
            "lon": row[5]
        })

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)