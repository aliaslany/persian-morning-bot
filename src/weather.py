import requests

def get_aliabad_weather():
    """
    Fetches the current weather for Aliabad-e-Katul using wttr.in.
    """
    try:
        response = requests.get("https://wttr.in/Aliabad-e-Katul?format=3&m", timeout=5)
        if response.status_code == 200:
            return response.text.strip()
    except Exception as e:
        print(f"Error fetching weather: {e}")
        
    return None
