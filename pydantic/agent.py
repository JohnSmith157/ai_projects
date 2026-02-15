from pydantic_ai import Agent
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the agent with the specified model and instructions
agent = Agent(
    'openai:gpt-5-mini',
    instructions='Answer in a short way.',
)

async def get_agent_response(user_input: str) -> str:
    try:
        # Run the agent asynchronously
        result = await agent.run(user_input)
        return result.output
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Test the agent directly
    print(get_agent_response("Hello, how are you?"))
