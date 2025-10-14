from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from backend.data_tools import (
    get_revenue_vs_budget,
    get_gross_margin,
    get_opex_breakdown,
    get_cash_runway,
)

def create_agent():
    # Define your tools
    tools = [
        Tool(name="Revenue vs Budget", func=get_revenue_vs_budget, description="Compare actual and budget revenue for a given month."),
        Tool(name="Gross Margin", func=get_gross_margin, description="Show gross margin trend or for a given month."),
        Tool(name="Opex Breakdown", func=get_opex_breakdown, description="Break down operating expenses by category."),
        Tool(name="Cash Runway", func=get_cash_runway, description="Estimate remaining cash runway."),
    ]

    # Use GPT-4 or GPT-3.5 as reasoning engine
    llm = ChatOpenAI(model="gpt-4", temperature=0)

    # Initialize the LangChain agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type="zero-shot-react-description",
        verbose=True
    )

    return agent
