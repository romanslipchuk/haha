import os
import asyncio
from dotenv import load_dotenv

from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters

from langchain_gigachat import GigaChat
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.tools import load_mcp_tools

# Загружаем API-ключ
load_dotenv()
GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")

async def run_client():
    # Initialize GigaChat model
    model = GigaChat(model="GigaChat", credentials=GIGACHAT_API_KEY, verify=False)
    print("GigaChat model initialized.")

    # Configure server parameters
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"],  # Убедись, что путь к серверу верный
    )
    print("Debugging server params:", server_params)

    # Debugging: Print API key
    print("GIGACHAT_API_KEY:", GIGACHAT_API_KEY)

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Session initialized.")

            # Load tools
            tools = await load_mcp_tools(session)
            print("Loaded tools:", tools)

            # Create agent
            agent = create_react_agent(model, tools)
            print("Agent created.")

            # Send request to agent
            response = await agent.ainvoke({
                "messages": [{"role": "user", "content": "Как мне стать хорошим Data Scientist?"}]
            })
            print("Ответ от агента:", response)

if __name__ == "__main__":
    asyncio.run(run_client())