import asyncio
from fastmcp import FastMCP, Client

test_client = Client("mcp-server.py")

async def call_mcp_tool( name : str ): 
    async with test_client as client:
        result = await client.call_tool( "greet", {"name": name})
        print(result)

asyncio.run(call_mcp_tool("Partha"))

