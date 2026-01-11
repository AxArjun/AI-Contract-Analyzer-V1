from typing import TypedDict
from langgraph.graph import StateGraph, END

from services.planner import plan_agents

from agents.legal_agent import legal_agent
from agents.finance_agent import finance_agent
from agents.compliance_agent import compliance_agent
from agents.operations_agent import operations_agent


# -------------------------------
# State Definition
# -------------------------------
class ContractState(TypedDict, total=False):
    text: str
    plan: dict
    legal: str
    finance: str
    compliance: str
    operations: str


# -------------------------------
# Planner Node
# -------------------------------
def planner_node(state: ContractState):
    plan = plan_agents(state["text"])
    return {"plan": plan}


# -------------------------------
# Agent Nodes (Condition-aware)
# -------------------------------
def legal_node(state: ContractState):
    if state["plan"].get("legal"):
        return {"legal": legal_agent(state["text"])}
    return {}

def finance_node(state: ContractState):
    if state["plan"].get("finance"):
        return {"finance": finance_agent(state["text"])}
    return {}

def compliance_node(state: ContractState):
    if state["plan"].get("compliance"):
        return {"compliance": compliance_agent(state["text"])}
    return {}

def operations_node(state: ContractState):
    if state["plan"].get("operations"):
        return {"operations": operations_agent(state["text"])}
    return {}


# -------------------------------
# Build LangGraph (PARALLEL)
# -------------------------------
graph = StateGraph(ContractState)

graph.add_node("planner", planner_node)
graph.add_node("legal", legal_node)
graph.add_node("finance", finance_node)
graph.add_node("compliance", compliance_node)
graph.add_node("operations", operations_node)

# Entry point
graph.set_entry_point("planner")

# 🔥 Planner → Parallel agents
graph.add_edge("planner", "legal")
graph.add_edge("planner", "finance")
graph.add_edge("planner", "compliance")
graph.add_edge("planner", "operations")

# End nodes
graph.add_edge("legal", END)
graph.add_edge("finance", END)
graph.add_edge("compliance", END)
graph.add_edge("operations", END)

contract_graph = graph.compile()


# -------------------------------
# Public API Function
# -------------------------------
def analyze_with_agents(text: str):
    """
    Executes planner-driven, parallel multi-agent analysis
    """
    result = contract_graph.invoke({"text": text})

    return {
        "legal": result.get("legal"),
        "finance": result.get("finance"),
        "compliance": result.get("compliance"),
        "operations": result.get("operations"),
    }
