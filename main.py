
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the vulnerable app!"

@app.route("/search")
def search():
    query = request.args.get("q")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = '%s'" % query)
    results = cursor.fetchall()
    return str(results)

if __name__ == "__main__":
    app.run(debug=True)
