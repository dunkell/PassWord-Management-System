import sqlite3

from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, get_db_connection

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                       (data['username'], data['email'], hashed_password))
        conn.commit()
        return jsonify({"message": "User registered successfully!"})
    except sqlite3.IntegrityError:
        return jsonify({"message": "Username or email already exists!"}), 400
    finally:
        conn.close()