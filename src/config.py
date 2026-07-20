import os
from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_ID = os.getenv("CHANNEL_ID")


CHANNEL_NAME = os.getenv(
    "CHANNEL_NAME",
    "کانال صبحانه"
)


CHANNEL_LINK = os.getenv(
    "CHANNEL_LINK",
    "https://t.me/your_channel"
)


if not BOT_TOKEN:
    raise Exception("BOT_TOKEN is missing")

if not CHANNEL_ID:
    raise Exception("CHANNEL_ID is missing")
