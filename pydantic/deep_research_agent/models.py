from pydantic import BaseModel, Field
from typing import List, Optional

class ResearchAngle(BaseModel):
    keyword: str = Field(description="Search keyword/phrase for deep research.")
    reason: str = Field(description="Why this angle is important.")

class ResearchPlan(BaseModel):
    is_ticker: bool = Field(description="Whether the query is a stock ticker.")
    entity_name: str = Field(description="Resolved full name of the ticker or entity.")
    context: str = Field(description="Context or industry of the discovered entity.")
    angles: List[ResearchAngle] = Field(description="3-4 distinct research angles.")

class Fact(BaseModel):
    content: str = Field(description="A key fact or number found.")
    source_url: str = Field(description="URL of the source.")
    source_title: str = Field(description="Title of the source.")

class Section(BaseModel):
    title: str = Field(description="Title of the research section (based on angle).")
    findings: str = Field(description="Detailed synthesis of findings for this section (markdown).")
    key_facts: List[Fact] = Field(description="List of key facts supporting the findings.")

class ResearchReport(BaseModel):
    executive_summary: str = Field(description="High-level summary of the entire research.")
    sections: List[Section] = Field(description="Detailed sections.")
    risks_uncertainties: str = Field(description="Identified risks, uncertainties, or conflicting info.")
    what_to_watch: List[str] = Field(description="List of future events or metrics to watch.")
