from flask import Flask, request, jsonify
import os, psycopg2

app = Flask(__name__)
conn = psycopg2.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

@app.route("/save", methods=["POST"])
def save():
    text = request.json.get("text", "")
    cur.execute("INSERT INTO logs(content) VALUES (%s)", (text,))
    conn.commit()
    return jsonify({"status":"saved"})
