import json
import os
import random
import requests

def get_random_poem():
    """
    Tries to get a random poem from Ganjoor API (c.ganjoor.net).
    Falls back to local poems.json if API fails.
    """
    try:
        response = requests.get("https://c.ganjoor.net/beyt-json.php", timeout=5)
        if response.status_code == 200:
            data = response.json()
            m1 = data.get("m1", "")
            m2 = data.get("m2", "")
            poet = data.get("poet", "")
            if m1 and m2:
                poem_text = f"{m1}\n{m2}"
                if poet:
                    poem_text += f"\n(شاعر: {poet})"
                return poem_text
    except Exception as e:
        print(f"Error fetching from Ganjoor API: {e}")

    print("Falling back to local poems...")
    try:
        # Fallback to local
        poems_file = os.path.join(os.path.dirname(__file__), "..", "data", "poems.json")
        if os.path.exists(poems_file):
            with open(poems_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            if data:
                return random.choice(data)
    except Exception as e:
        print(f"Error loading local poems: {e}")
        
    return "توانا بود هر که دانا بود\nز دانش دل پیر برنا بود"
