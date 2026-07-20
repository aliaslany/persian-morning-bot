import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
CHANNEL_NAME = os.getenv("CHANNEL_NAME", "کانال صبحانه")
CHANNEL_LINK = os.getenv("CHANNEL_LINK", "https://t.me/your_channel")

# We can bypass this if running tests without token
if not BOT_TOKEN and os.getenv("ENV") != "test":
    print("Warning: BOT_TOKEN is missing")
    
if not CHANNEL_ID and os.getenv("ENV") != "test":
    print("Warning: CHANNEL_ID is missing")
