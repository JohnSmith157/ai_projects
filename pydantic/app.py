import gradio as gr
from agent import get_agent_response

async def chat_interface(message, history):
    return await get_agent_response(message)

# Create the Gradio interface
demo = gr.ChatInterface(
    fn=chat_interface,
    title="Simple Pydantic AI Agent",
    description="Ask me anything! I'm powered by gpt-5-mini and Pydantic AI.",
    examples=["What is the capital of France?", "Tell me a joke.", "Explain quantum physics briefly."],
)

if __name__ == "__main__":
    demo.launch()
