import json
import os
import random

def get_random_greeting():
    """
    Get a random morning greeting from local JSON.
    """
    greetings_file = os.path.join(os.path.dirname(__file__), "..", "data", "greetings.json")
    if os.path.exists(greetings_file):
        try:
            with open(greetings_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            if data:
                return random.choice(data)
        except Exception as e:
            print(f"Error loading greetings: {e}")
            
    return "سلام! صبح بخیر 🌞\nامیدوارم روز فوق‌العاده‌ای داشته باشید."
