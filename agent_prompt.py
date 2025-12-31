import os
import requests
from dotenv import load_dotenv
from groq import Groq
import json

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Returns the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name, e.g., Toronto,CA"
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Returns the current date and time.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]

# Load API keys and initialize client
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MCP_SERVER = "http://127.0.0.1:8000"

# --- Function to call MCP endpoints ---
def call_mcp_tool(function_name, arguments):
    if function_name == "get_current_weather":
        location = arguments.get("location")
        response = requests.get(f"{MCP_SERVER}/weather", params={"location": location})
        return response.json()
    elif function_name == "get_current_time":
        response = requests.get(f"{MCP_SERVER}/time")
        return response.json()
    else:
        return {"error": "Unknown tool"}

# --- Function calling agent ---
def gpt_agent(prompt):
    
    model = "openai/gpt-oss-120b"
    messages = [{"role": "user", "content": prompt}]

    while True:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        # print(response)

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            return message.content


        for call in message.tool_calls:
            func_name = call.function.name
            arguments = json.loads(call.function.arguments)
            tool_result = call_mcp_tool(func_name, arguments)

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "name": func_name,
                "content": json.dumps(tool_result)
            })

# --- Run the agent interactively ---
if __name__ == "__main__":
    while True:
        user_input = input("Ask the agent: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = gpt_agent(user_input)
        print("Agent:", answer)

