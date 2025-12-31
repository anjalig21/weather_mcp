import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_current_weather(location: str) -> dict:
    """
    Fetches the current weather for a given location.
    
    Args:
        location (str): City name (e.g., "Toronto, ON")
    
    Returns:
        dict: Temperature, condition, and wind speed
    
    Raises:
        ValueError: If API key is not set
        requests.exceptions.HTTPError: If API request fails
    """
    if not WEATHER_API_KEY:
        raise ValueError(
            "WEATHER_API_KEY environment variable is not set. "
            "Please create a .env file with: WEATHER_API_KEY=your_api_key_here"
        )
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": WEATHER_API_KEY,
        "units": "metric"  # Celsius
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 401:
        raise ValueError(
            "Invalid or expired OpenWeatherMap API key. "
            "Please check your API key at https://home.openweathermap.org/api_keys"
        )
    
    response.raise_for_status()
    data = response.json()

    return {
        "location": location,
        "temperature_c": data["main"]["temp"],
        "condition": data["weather"][0]["description"],
        "wind_kph": data["wind"]["speed"]
    }

if __name__ == "__main__":
    location = "Toronto,CA"  # you can change this
    print(get_current_weather(location))
