from datetime import datetime

def get_current_date_time() -> dict:
    """
    Returns the current local date and time as a dictionary.
    """
    now = datetime.now()
    print(now)

    ## We return a dictionary because MCP tools return structured JSON-like data
    return {
        "date": now.strftime("%Y-%m-%d"),       # e.g., "2025-12-31"
        "time": now.strftime("%H:%M"),          # e.g., "14:30"
        "weekday": now.strftime("%A")           # e.g., "Wednesday"
    }
    