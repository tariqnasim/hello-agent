################################
# Assignment#2  agent_hello.py #
################################

# ensure if using vscode the interpreter is correctly selected from .venv\Scripts\python.exe that was created by UV

# using dotenv to load API_KEY from .env

from dotenv import load_dotenv 
import os

# Loading environment variables from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Implementing the agent logic inside the function my_first_agent using the OpenAI Agent SDK
def my_first_agent():
    if api_key: # Check condition to be true
        print("\n Hello, world! my_first_agent")
    else:
        print("Missing API key. Please .env file or check OPENAI_API_KEY parameter definition.")

if __name__ == "__main__": # Running from within
    my_first_agent()
