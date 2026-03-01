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

if __name__ == "__main__":
    mcp.run(transport="stdio")
