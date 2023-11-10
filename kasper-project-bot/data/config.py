import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__name__).resolve().parent
ENV_FILE = BASE_DIR / '.env'


if os.path.exists(ENV_FILE):
    load_dotenv(ENV_FILE)

BOT_TOKEN = os.getenv('BOT_TOKEN')
SERVER_URL = str(os.getenv('SERVER_URL'))