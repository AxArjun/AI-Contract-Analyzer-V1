from langchain_google_genai import ChatGoogleGenerativeAI
from agents.prompts import BASE_INSTRUCTIONS, FINANCE_PROMPT

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0
)

def finance_agent(text: str):
    prompt = f"""
{BASE_INSTRUCTIONS}

{FINANCE_PROMPT}

Analyze the contract from a financial perspective.

Return the response strictly in JSON format with the following fields:
- payment_terms
- penalties
- tax_risks
- high_risk_clauses

Contract Text:
{text}
"""
    return llm.invoke(prompt).content
