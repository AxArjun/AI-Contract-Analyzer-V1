from langchain_google_genai import ChatGoogleGenerativeAI
from agents.prompts import BASE_INSTRUCTIONS, COMPLIANCE_PROMPT

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0
)

def compliance_agent(text: str):
    prompt = f"""
{BASE_INSTRUCTIONS}

{COMPLIANCE_PROMPT}

Analyze the contract for regulatory and compliance risks.

Return the response strictly in JSON format with the following fields:
- regulatory_requirements
- compliance_risks
- data_protection_issues
- audit_obligations
- red_flags

Contract Text:
{text}
"""
    return llm.invoke(prompt).content
