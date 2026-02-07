import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
EMAIL_ACCOUNT = os.getenv("E_ACCOUNT")
EMAIL_PASSWORD = os.getenv("E_PASSWORD")
CREDENTIALS = os.getenv("CREDENTIALS")
SHEET_ID = os.getenv("SHEET_ID")