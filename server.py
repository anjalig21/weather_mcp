from fastapi import FastAPI
from tools.weather_tool import get_current_weather
from tools.time_tool import get_current_date_time

app = FastAPI(title="MCP Agent Tools")

# --- Time Tool Endpoint ---
@app.get("/time")
def time_endpoint():
    """
    Returns current date and time.
    """
    return get_current_date_time()

# --- Weather Tool Endpoint ---
@app.get("/weather")
def weather_endpoint(location: str):
    """
    Returns current weather for a given location.
    Example: /weather?location=Toronto,CA
    """
    return get_current_weather(location)
