from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Correct path for SQLite file
DB_PATH = os.path.join(os.path.dirname(__file__), "services.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ----------------------
# Home page
# ----------------------
@app.route("/")
def home():
    return render_template("main.html", page_type="home")

# ----------------------
# Search services
# ----------------------
@app.route("/search", methods=["GET"])
def search():
    location = request.args.get("location", "").strip()
    service_type = request.args.get("service", "").strip()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM services
        WHERE location LIKE ? AND type LIKE ?
        ORDER BY rating DESC
    """, (f"%{location}%", f"%{service_type}%"))
    results = cur.fetchall()
    conn.close()
    return render_template("main.html", page_type="search", results=results)

# ----------------------
# Trish AI assistant
# ----------------------
@app.route("/ai", methods=["GET"])
def ai():
    question = request.args.get("question", "").strip().lower()
    conn = get_db()
    cur = conn.cursor()

    results = []

    if "best" in question or "recommend" in question:
        cur.execute("SELECT * FROM services ORDER BY rating DESC LIMIT 3")
        results = cur.fetchall()
    elif any(x in question for x in ["hospital", "school", "hotel", "restaurant", "atm", "petrol"]):
        cur.execute("SELECT * FROM services WHERE type LIKE ? ORDER BY rating DESC LIMIT 3", (f"%{question}%",))
        results = cur.fetchall()
    else:
        results = [
            {"name": "Try asking about best hospitals, hotels, or schools", "type":"", "location":"", "rating":""},
            {"name": "Ask for directions or contact info of a service", "type":"", "location":"", "rating":""},
            {"name": "You can ask which service is recommended in a specific area", "type":"", "location":"", "rating":""}
        ]

    conn.close()
    return render_template("main.html", page_type="ai", results=results, ai_name="Trish AI")

# ----------------------
# Run server
# ----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)