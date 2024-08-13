from flask import Flask
import os
import sqlite3

app = Flask(__name__)

# 配置 SQLite 数据库
app.config['DATABASE'] = os.path.join(os.getcwd(), 'app', 'database.db')
app.config['SECRET_KEY'] = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

from app import routes