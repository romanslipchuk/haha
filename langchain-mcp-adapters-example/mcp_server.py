import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from gigachat import GigaChat


# Инициализация GigaChat SDK
giga = GigaChat(
    scope="GIGACHAT_API_PERS",
    model="GigaChat"
)

# Создаем MCP сервер
mcp = FastMCP("GigaChatServer")

@mcp.tool()
def chat(prompt: str) -> str:
    """Отправляет запрос в GigaChat и возвращает ответ"""
    response = giga.chat_completions(messages=[{"role": "user", "content": prompt}])
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    print("mcp server started")
    mcp.run(transport="stdio")
