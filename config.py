import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, 'app', 'database.db')
SECRET_KEY = 'your_secret_key'
