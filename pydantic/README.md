# Simple Pydantic AI Agent with Gradio

This project implements a simple AI agent using [Pydantic AI](https://ai.pydantic.dev/) and provides a web interface using [Gradio](https://www.gradio.app/).

## Prerequisites

- Python 3.10+
- OpenAI API Key

## Setup

1.  **Clone the repository** (or navigate to this folder):
    ```bash
    cd simple_agent
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**:
    - Open the `.env` file.
    - Replace `your_openai_api_key_here` with your actual OpenAI API key.

## Usage

1.  **Run the application**:
    ```bash
    python app.py
    ```

2.  **Access the interface**:
    - Open your browser and navigate to the URL provided in the terminal (usually `http://127.0.0.1:7860`).

3.  **Interact with the Agent**:
    - Type your message in the chat box and press Enter.

## Project Structure

- `agent.py`: Contains the logic for the Pydantic AI agent.
- `app.py`: Defines the Gradio web interface.
- `.env`: Stores configuration secrets (API keys).
- `requirements.txt`: Python package dependencies.
