from fastmcp import FastMCP

mcp = FastMCP("Hello world MCP server.")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello world! {name}"

if __name__ == "__main__":
    # mcp.run() # what is the default? stdio ? 
    mcp.run( transport= "stdio") 
