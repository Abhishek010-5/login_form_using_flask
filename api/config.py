import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
DB_URI = os.getenv("URI")
DB = os.getenv("DB")
SECRET_KEY = os.getenv("SECRET_KEY")
PASSWORD = os.getenv("PASSWORD")
MAIL = os.getenv("MAIL")