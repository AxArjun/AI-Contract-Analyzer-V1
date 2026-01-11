from langchain_google_genai import ChatGoogleGenerativeAI
from agents.prompts import BASE_INSTRUCTIONS, LEGAL_PROMPT

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0
)

def legal_agent(text: str):
    prompt = f"""
{BASE_INSTRUCTIONS}
{LEGAL_PROMPT}

Contract Text:
{text}
"""
    return llm.invoke(prompt).content
