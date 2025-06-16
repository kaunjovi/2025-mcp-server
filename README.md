# 2025-mcp-server
2025 MCP server using python. 


1. Use uv to initiate a project 
```
uv init
Initialized project `2025-mcp-server`

uv venv 
Using CPython 3.11.9 interpreter at: /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate


```

1. Check that it is using the .venv location 
```
where python
/Users/kaunjovi/code/2025-mcp-server/.venv/bin/python
```

1. Run the default python 
```
python main.py
Hello from 2025-mcp-server!
```


uv add langchain-groq langchain-mcp-adapters mcp 

## Welcome to FastMCP 2.0!
1. https://gofastmcp.com/getting-started/welcome

## How can you connect to your MCP server tool ? 

1. **mcp.run( transport= "stdio")** 
1. Use the standard input and output ( stdin stdout) io. 
1. Run the server in command prompt. 
1. Great for local testing. 


## LangGraph Trainining 

1. https://academy.langchain.com/courses/take/intro-to-langgraph/lessons/58238107-course-overview

## [Build Smarter AI Agents for Free Using LangGraph & Ollama](https://medium.com/data-science-collective/build-smarter-ai-agents-for-free-using-langgraph-ollama-9096ad7952aa)


