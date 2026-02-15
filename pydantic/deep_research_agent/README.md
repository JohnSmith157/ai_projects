# Deep Research Agent 🕵️‍♂️

A powerful multi-agent research system built with Pydantic AI that performs comprehensive deep research on any topic or stock ticker. The agent automatically plans research strategies, executes parallel web searches, fetches and analyzes content, and synthesizes professional reports with citations.

## 🌟 Features

- **Intelligent Intent Detection**: Automatically detects whether input is a stock ticker or general topic
- **Strategic Planning**: Generates 3-4 unique research angles tailored to the subject
- **Deep Web Search**: Uses DuckDuckGo to find relevant, up-to-date sources
- **Content Parsing**: Fetches and reads clean text from web pages for deeper analysis
- **Parallel Processing**: Conducts research on multiple angles simultaneously for speed
- **Structured Synthesis**: Produces markdown reports with executive summaries, detailed sections, citations, risk analysis, and future watchlist items

## 📁 Project Structure

```
deep_research_agent/
├── models.py          # Pydantic models for structured data
├── tools.py           # DuckDuckGo search and web scraping utilities
├── agent.py           # Core multi-agent workflow logic
├── app.py             # Gradio web interface
├── requirements.txt   # Python dependencies
├── .env              # Environment variables (API keys)
└── README.md         # This file
```

### File Descriptions

#### `models.py`
Defines Pydantic models for structured outputs:
- **`ResearchAngle`**: Represents a single research angle with keyword and rationale
- **`ResearchPlan`**: Contains the overall research strategy (entity name, context, angles)
- **`Fact`**: Stores individual facts with source attribution
- **`Section`**: Represents a report section with findings and supporting facts
- **`ResearchReport`**: The complete report structure with executive summary, sections, risks, and watchlist

#### `tools.py`
Contains utility functions for web research:
- **`search_duckduckgo(query, max_results)`**: Searches DuckDuckGo and returns results
- **`fetch_page_content(url, timeout)`**: Fetches and parses web page content using BeautifulSoup and html2text

#### `agent.py`
Implements the core multi-agent workflow:
- **Planner Agent**: Analyzes the query, detects intent (ticker vs. general), and generates research angles
- **Writer Agent**: Synthesizes all research findings into a comprehensive report
- **`perform_deep_research(user_query)`**: Orchestrates the 3-step workflow:
  1. **Planning Phase**: Creates research strategy
  2. **Research Phase**: Executes parallel searches and content fetching
  3. **Synthesis Phase**: Compiles findings into a structured markdown report

#### `app.py`
Gradio web interface that provides:
- Chat-based interface for submitting queries
- Real-time research progress updates
- Markdown-formatted report display
- Example queries for quick testing

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Git (for cloning the repository)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd agentic-ai-bootcamp/pydantic/deep_research_agent
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - Open the `.env` file
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

### Running the Application

1. **Start the Gradio interface**:
   ```bash
   python app.py
   ```

2. **Access the web interface**:
   - Open your browser and navigate to: `http://127.0.0.1:7860`
   - The interface will display with example queries

3. **Try it out**:
   - Enter a stock ticker (e.g., `NVDA`, `TSLA`, `AAPL`)
   - Or enter a general research query (e.g., `What is the future of solid state batteries?`)
   - Watch as the agent plans, researches, and synthesizes a comprehensive report

## 📊 Example Queries

- **Stock Tickers**: `NVDA`, `TSLA`, `AAPL`, `MSFT`
- **Technology Topics**: `What is the future of quantum computing?`, `SpaceX Starship progress`
- **Industry Research**: `Electric vehicle market trends`, `AI chip competition`
- **Emerging Tech**: `Solid state battery development`, `Nuclear fusion breakthroughs`

## 🔧 How It Works

1. **User submits a query** through the Gradio interface
2. **Planner Agent** analyzes the query:
   - Detects if it's a stock ticker or general topic
   - Resolves company names and industry context
   - Generates 3-4 strategic research angles
3. **Research Phase** executes in parallel:
   - Each angle triggers DuckDuckGo searches
   - Top results are fetched and parsed for content
   - Facts and sources are collected
4. **Writer Agent** synthesizes the report:
   - Compiles all research findings
   - Structures information into sections
   - Adds citations, risk analysis, and future watchlist
5. **Markdown report** is displayed in the interface

## 🛠️ Customization

### Changing the LLM Model
Edit `agent.py` and modify the model string in the Agent definitions:
```python
planner_agent = Agent(
    'openai:gpt-4',  # Change this to your preferred model
    output_type=ResearchPlan,
    ...
)
```

### Adjusting Search Depth
Modify the `max_results` parameter in `agent.py`:
```python
results = search_duckduckgo(query, max_results=5)  # Increase for more sources
```

### Customizing Report Structure
Edit the Pydantic models in `models.py` to add or modify report sections.

## 📝 Dependencies

- **pydantic-ai**: Agent framework
- **gradio**: Web interface
- **python-dotenv**: Environment variable management
- **openai**: LLM provider
- **duckduckgo-search**: Web search functionality
- **beautifulsoup4**: HTML parsing
- **requests**: HTTP requests
- **html2text**: HTML to markdown conversion

## 🐛 Troubleshooting

### API Key Issues
- Ensure your `.env` file contains a valid `OPENAI_API_KEY`
- Restart the application after updating the `.env` file

### DuckDuckGo Search Warnings
- If you see warnings about `duckduckgo_search` being renamed, you can safely ignore them or update to `ddgs` package

### Slow Performance
- Research depth can be adjusted by reducing `max_results` in search calls
- Consider using a faster LLM model like `gpt-3.5-turbo`

## 📄 License

This project is part of the Agentic AI Bootcamp.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

**Built with ❤️ using Pydantic AI**
