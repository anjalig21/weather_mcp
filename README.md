# Weather MCP Agent

An AI-powered agent that uses Groq's LLM API to answer questions about weather and time. The agent can call external tools (MCP server endpoints) to fetch real-time weather data and current time information.

## Features

- 🤖 **AI Agent**: Powered by Groq's LLM (using `openai/gpt-oss-120b` model)
- 🌤️ **Weather Information**: Get current weather for any city
- ⏰ **Time Information**: Get current date and time
- 🔧 **Function Calling**: Automatic tool selection and execution
- 🚀 **FastAPI Server**: RESTful API endpoints for tools

## Prerequisites

- Python 3.10 or higher
- Groq API key (free at [console.groq.com](https://console.groq.com))
- OpenWeatherMap API key (free at [openweathermap.org](https://openweathermap.org/api))

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anjalig21/weather_mcp.git
   cd weather_mcp
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   
   Create a `.env` file in the project root:
   ```bash
   touch .env
   ```
   
   Add your API keys to `.env`:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   WEATHER_API_KEY=your_openweathermap_api_key_here
   ```

## Usage

### 1. Start the MCP Server

In one terminal, start the FastAPI server:

```bash
uvicorn server:app --reload
```

The server will run at `http://127.0.0.1:8000`

### 2. Run the Agent

In another terminal, run the agent:

```bash
python3 agent_prompt.py
```

### 3. Interact with the Agent

The agent will prompt you for questions. You can ask:

- "What is the weather in Toronto, ON?"
- "What's the time and weather in New York?"
- "Tell me the current time"
- Type `exit` or `quit` to stop

## Project Structure

```
weather_mcp/
├── agent_prompt.py      # Main agent script with Groq integration
├── server.py            # FastAPI server with tool endpoints
├── tools/
│   ├── weather_tool.py  # Weather API integration
│   └── time_tool.py     # Time utility
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
└── README.md           # This file
```

## API Endpoints

The MCP server exposes the following endpoints:

- `GET /weather?location={city}` - Get current weather for a location
- `GET /time` - Get current date and time

## Technologies Used

- **Groq**: LLM API for AI agent
- **FastAPI**: Web framework for the MCP server
- **OpenWeatherMap API**: Weather data
- **Python-dotenv**: Environment variable management
- **Requests**: HTTP library for API calls

## Configuration

### Groq API Key

1. Sign up at [console.groq.com](https://console.groq.com)
2. Create an API key
3. Add it to your `.env` file as `GROQ_API_KEY`

### OpenWeatherMap API Key

1. Sign up at [openweathermap.org](https://openweathermap.org/api)
2. Get your free API key (may take 1-2 hours to activate)
3. Add it to your `.env` file as `WEATHER_API_KEY`

## Model Options

You can change the Groq model in `agent_prompt.py`:

```python
model = "openai/gpt-oss-120b"  # Current model
```

Other available models:
- `llama-3.1-70b-versatile`
- `llama-3.1-8b-instant`
- `mixtral-8x7b-32768`

## Troubleshooting

### Server Connection Error
- Make sure the MCP server is running on port 8000
- Check that `uvicorn server:app --reload` is running

### API Key Errors
- Verify your API keys are correctly set in `.env`
- For OpenWeatherMap, wait 1-2 hours after creating the key for activation
- Check that `.env` is in the project root directory

### JSON Decode Errors
- Ensure the MCP server is running before starting the agent
- Check server logs for any errors

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to submit issues or pull requests!

