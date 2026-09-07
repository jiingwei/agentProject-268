import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from .tools import calculator
from rag.rag_tool import search_company_handbook

load_dotenv()


model = ChatOpenAI(
    model=os.getenv("MODEL_NAME", "deepseek-v4-flash"),
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    temperature=0,
)


tools = [
    calculator,
    search_company_handbook
]


agent = create_react_agent(
    model=model,
    tools=tools,
)









