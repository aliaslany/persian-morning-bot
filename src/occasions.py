import json
import os
import requests

CALENDAR_API_URL = "https://pnldev.com/api/calender"


def get_today_occasions(jalali_year: int, jalali_month: int, jalali_day: int, month_day_jalali: str = None):
    """
    Fetch today's occasions from the pnldev Jalali calendar API (live, accurate,
    covers the whole year). Falls back to the local JSON file (data/occasions.json)
    if the API is unreachable or returns something unexpected.
    """
    try:
        response = requests.get(
            CALENDAR_API_URL,
            params={"year": jalali_year, "month": jalali_month, "day": jalali_day},
            timeout=5,
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("status"):
                events = data.get("result", {}).get("event", [])
                if events:
                    return events
                return []
    except Exception as e:
        print(f"Error fetching occasions from API: {e}")

    # Fallback to local JSON data
    return _get_occasions_from_local_file(month_day_jalali or f"{jalali_month}-{jalali_day}")


def _get_occasions_from_local_file(month_day_jalali: str):
    occasions_file = os.path.join(os.path.dirname(__file__), "..", "data", "occasions.json")
    if not os.path.exists(occasions_file):
        return []

    try:
        with open(occasions_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data.get(month_day_jalali, [])
    except Exception as e:
        print(f"Error loading occasions from local file: {e}")
        return []
