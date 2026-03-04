from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Calculator")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together.
    
    Args:
        a: The first number.
        b: The second number.
    """
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first.
    
    Args:
        a: The number to subtract from.
        b: The number to subtract.
    """
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.
    
    Args:
        a: The first number.
        b: The second number.
    """
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide the first number by the second.
    
    Args:
        a: The dividend.
        b: The divisor.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.resource("playbook://customer-support", mime_type="text/markdown")
def get_playbook() -> str:
    """Returns the customer support playbook."""
    with open("resource_example.md", "r", encoding="utf-8") as f:
        return f.read()

@mcp.prompt()
def webinar_to_blog(
    webinar_title: str,
    webinar_date: str,
    speakers: str,
    transcript: str
) -> str:
    """A prompt for converting webinar transcripts into refined blog posts."""
    with open("prompt.md", "r", encoding="utf-8") as f:
        template = f.read()
    
    return (template
            .replace("{{ webinar_title }}", webinar_title)
            .replace("{{ webinar_date }}", webinar_date)
            .replace("{{ speakers }}", speakers)
            .replace("{{ transcript }}", transcript))




if __name__ == "__main__":
    mcp.run(transport="stdio")
