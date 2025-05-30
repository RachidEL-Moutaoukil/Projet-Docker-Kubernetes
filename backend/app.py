from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the backend!"})

@app.route('/db')
def test_db():
    conn = psycopg2.connect(
        dbname="appdb",
        user="admin",
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    now = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({"db_time": now})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
