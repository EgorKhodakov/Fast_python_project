import os
from dotenv import load_dotenv

load_dotenv()
VALID_EMAIL = os.getenv("GITHUB_VALID_EMAIL")
VALID_PASSWORD = os.getenv("GITHUB_VALID_PASSWORD")
VALID_USERNAME = os.getenv("GITHUB_VALID_USERNAME")