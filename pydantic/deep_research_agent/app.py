import gradio as gr
from agent import perform_deep_research
import asyncio

async def run_research(query, history):
    # History is ignored for this specific deep research tool as it is a one-shot report generator
    return await perform_deep_research(query)

demo = gr.ChatInterface(
    fn=run_research,
    title="Deep Research Agent",
    description="Enter a Stock Ticker (e.g., NVDA, TSLA) or a General Query. I will generate a comprehensive research report.",
    examples=["NVDA", "What is the future of solid state batteries?", "AAPL", "SpaceX Starship progress"],
)

if __name__ == "__main__":
    demo.launch()
