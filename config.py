import os
from dotenv import load_dotenv

load_dotenv()
VALID_USERNAME = os.getenv("GITHUB_VALID_USERNAME")
VALID_PASSWORD = os.getenv("GITHUB_VALID_PASSWORD")