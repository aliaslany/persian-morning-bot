import requests
import datetime

def get_tehran_prayer_times():
    """
    Fetches the prayer times for Tehran using Aladhan API.
    """
    try:
        url = "https://api.aladhan.com/v1/timingsByCity"
        params = {
            "city": "Tehran",
            "country": "Iran",
            "method": 8 # Gulf Region or standard for Iran (often 7 or 8)
        }
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            timings = data.get("data", {}).get("timings", {})
            if timings:
                return {
                    "fajr": timings.get("Fajr"),
                    "sunrise": timings.get("Sunrise"),
                    "dhuhr": timings.get("Dhuhr"),
                    "asr": timings.get("Asr"),
                    "maghrib": timings.get("Maghrib"),
                    "isha": timings.get("Isha")
                }
    except Exception as e:
        print(f"Error fetching prayer times: {e}")
        
    return None
