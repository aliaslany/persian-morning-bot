import requests
import time
from src.config import BOT_TOKEN

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id: str, text: str):
    """Send text message to Telegram channel"""
    if not BOT_TOKEN:
        print("BOT_TOKEN not set, skipping actual send_message")
        return None
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    response = requests.post(url, data=payload, timeout=20)
    response.raise_for_status()
    return response.json()

def send_photo(chat_id: str, image_path: str, caption: str):
    """Send photo with Persian caption"""
    if not BOT_TOKEN:
        print("BOT_TOKEN not set, skipping actual send_photo")
        return None
    url = f"{TELEGRAM_API}/sendPhoto"
    for attempt in range(3):
        try:
            with open(image_path, "rb") as photo:
                files = {"photo": photo}
                data = {
                    "chat_id": chat_id,
                    "caption": caption,
                    "parse_mode": "HTML"
                }
                response = requests.post(url, data=data, files=files, timeout=30)
                response.raise_for_status()
                return response.json()
        except Exception as error:
            print(f"خطا در ارسال عکس، تلاش {attempt+1}/3")
            print(error)
            time.sleep(5)
    raise Exception("ارسال عکس به تلگرام ناموفق بود")
