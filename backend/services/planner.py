from langchain_google_genai import ChatGoogleGenerativeAI
from agents.prompts import BASE_INSTRUCTIONS, PLANNER_PROMPT

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0
)

KEYWORDS = {
    "legal": ["law", "jurisdiction", "termination", "liability"],
    "finance": ["payment", "invoice", "fee", "tax"],
    "compliance": ["gdpr", "compliance", "regulation", "audit"],
    "operations": ["service", "sla", "delivery", "support"]
}

def keyword_fallback(text: str):
    domains = []
    for domain, keys in KEYWORDS.items():
        if any(k.lower() in text.lower() for k in keys):
            domains.append(domain)
    return domains or ["legal"]

# ✅ THIS NAME MUST EXIST
def plan_agents(contract_text: str):
    prompt = f"""
{BASE_INSTRUCTIONS}
{PLANNER_PROMPT}

Contract Text:
{contract_text}

Respond ONLY in JSON:
{{
  "legal": true,
  "finance": true,
  "compliance": true,
  "operations": true
}}
"""

    try:
        response = llm.invoke(prompt).content
        return eval(response)
    except Exception:
        domains = keyword_fallback(contract_text)
        return {
            "legal": "legal" in domains,
            "finance": "finance" in domains,
            "compliance": "compliance" in domains,
            "operations": "operations" in domains
        }
