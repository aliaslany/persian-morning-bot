import json
import os

def get_today_occasions(month_day_jalali: str):
    """
    Load occasions from JSON file based on month-day format like '4-30'.
    """
    occasions_file = os.path.join(os.path.dirname(__file__), "..", "data", "occasions.json")
    if not os.path.exists(occasions_file):
        return []
    
    try:
        with open(occasions_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        return data.get(month_day_jalali, [])
    except Exception as e:
        print(f"Error loading occasions: {e}")
        return []
