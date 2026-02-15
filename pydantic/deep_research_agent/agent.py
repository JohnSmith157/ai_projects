from pydantic_ai import Agent, RunContext
from models import ResearchPlan, ResearchReport, Section, Fact
from tools import search_duckduckgo, fetch_page_content
import asyncio
from typing import List, Dict
from dotenv import load_dotenv

# --- Agents ---
load_dotenv()

# Planner Agent: Detects intent and generates angles
planner_agent = Agent(
    'openai:gpt-5-mini',
    output_type=ResearchPlan,
    instructions="""
    You are a Research Planner. Your goal is to understand the user's request.
    1. Determine if the input is a Stock Ticker (like 'NVDA') or a General Query.
    2. If it's a Ticker, identify the Company Name and Industry Context.
    3. Generate 3-4 distinct research angles (keywords) to investigate.
    
    If it is a general query, treat the input as the context.
    
    Examples of angles for stocks: 'Financial Performance', 'Competitive Landscape', 'Growth Drivers', 'Risks'.
    Examples for general: 'History', 'Key Technology', 'Market Size', 'Future Outlook'.
    """
)

# Writer Agent: Synthesizes findings into a report
writer_agent = Agent(
    'openai:gpt-5-mini',
    output_type=ResearchReport,
    instructions="""
    You are a Senior Equity Research Analyst and Technical Writer.
    Your goal is to write a comprehensive 'Deep Research Report' based on the provided research notes.
    
    You will be given a set of notes from different research angles.
    Structure the report clearly.
    
    IMPORTANT:
    - Use the provided search results to back up your claims.
    - Cite your sources by title and URL in the 'key_facts' sections.
    - Be objective and thorough.
    - Highlight risks and future watch items.
    """
)

# --- Workflow Logic ---

async def perform_deep_research(user_query: str) -> str:
    print(f"Starting research for: {user_query}")
    
    # 1. Planning Phase
    print("Step 1: Planning...")
    # Initial broad search to help the planner if needed (optional context injection)
    initial_search = search_duckduckgo(user_query, max_results=3)
    planner_context = f"User Query: {user_query}\nInitial Search Context: {initial_search}"
    
    # Run the planner agent
    plan_result = await planner_agent.run(planner_context)
    plan = plan_result.output
    
    print(f"Plan created: {plan.entity_name} ({plan.context})")
    print(f"Angles: {[a.keyword for a in plan.angles]}")
    
    # 2. Research Phase (Parallel)
    print("Step 2: Researching...")
    
    async def research_angle(angle) -> Dict:
        """Performs search and fetch for a single angle."""
        query = f"{plan.entity_name} {angle.keyword}"
        print(f"  Searching: {query}...")
        results = search_duckduckgo(query, max_results=3) # Top 3 per angle
        
        # Fetch content for top 1-2 results to get deep details
        angle_notes = []
        for res in results[:2]:
            content = fetch_page_content(res['href'])
            angle_notes.append({
                'title': res['title'],
                'url': res['href'],
                'snippet': res['body'],
                'full_content': content
            })
            
        return {
            'angle': angle.keyword,
            'reason': angle.reason,
            'notes': angle_notes
        }

    # Run all standard angle researches in parallel
    research_tasks = [research_angle(angle) for angle in plan.angles]
    research_results = await asyncio.gather(*research_tasks)
    
    # 3. Synthesis Phase
    print("Step 3: Synthesizing Report...")
    
    # Prepare context for the writer
    research_context = f"Subject: {plan.entity_name}\nContext: {plan.context}\n\n"
    for res in research_results:
        research_context += f"## Research Angle: {res['angle']}\n"
        research_context += f"Reason: {res['reason']}\n"
        for note in res['notes']:
            research_context += f"Source: {note['title']} ({note['url']})\n"
            research_context += f"Snippet: {note['snippet']}\n"
            research_context += f"Content (truncated): {note['full_content'][:1000]}\n\n"
            
    report_result = await writer_agent.run(research_context)
    report = report_result.output
    
    # 4. Format Output as Markdown
    markdown_output = f"# Deep Research Report: {plan.entity_name}\n\n"
    markdown_output += f"**Context**: {plan.context}\n\n"
    
    markdown_output += "## Executive Summary\n"
    markdown_output += f"{report.executive_summary}\n\n"
    
    for section in report.sections:
        markdown_output += f"## {section.title}\n"
        markdown_output += f"{section.findings}\n\n"
        markdown_output += "**Key Evidence:**\n"
        for fact in section.key_facts:
            markdown_output += f"- {fact.content} ([{fact.source_title}]({fact.source_url}))\n"
        markdown_output += "\n"
        
    markdown_output += "## Risks & Uncertainties\n"
    markdown_output += f"{report.risks_uncertainties}\n\n"
    
    markdown_output += "## What to Watch Next\n"
    for item in report.what_to_watch:
        markdown_output += f"- {item}\n"
        
    return markdown_output
