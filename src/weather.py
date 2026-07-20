import requests

def get_tehran_weather():
    """
    Fetches the current weather for Tehran using wttr.in.
    """
    try:
        response = requests.get("https://wttr.in/Tehran?format=3", timeout=5)
        if response.status_code == 200:
            return response.text.strip()
    except Exception as e:
        print(f"Error fetching weather: {e}")
        
    return None
