import os
import random
import requests

def get_random_image():
    """
    Downloads a random image from picsum.photos API.
    Saves it locally and returns the path. 
    Falls back to a random local image if API fails.
    """
    images_dir = os.path.join(os.path.dirname(__file__), "..", "data", "images")
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
        
    api_image_path = os.path.join(images_dir, "daily_downloaded.jpg")
    
    try:
        # Requesting a random 800x600 image
        response = requests.get("https://picsum.photos/800/600", timeout=10)
        if response.status_code == 200:
            with open(api_image_path, "wb") as f:
                f.write(response.content)
            return api_image_path
    except Exception as e:
        print(f"Error downloading image from API: {e}")
        
    print("Falling back to local images...")
    valid_extensions = ('.jpg', '.jpeg', '.png')
    images = [f for f in os.listdir(images_dir) if f.lower().endswith(valid_extensions)]
    
    if not images:
        return None
        
    chosen = random.choice(images)
    return os.path.join(images_dir, chosen)
