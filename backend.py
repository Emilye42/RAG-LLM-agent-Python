from backend.llm_agent import create_agent

agent = create_agent()

def process_query(query: str):
    try:
        response = agent.run(query)
        return response
    except Exception as e:
        return f"Error processing request: {e}"
