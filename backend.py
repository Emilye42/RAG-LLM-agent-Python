from agent.planner import process_query

def handle_user_query(question: str) -> str:
    """Bridge between frontend and agent logic."""
    try:
        response = process_query(question)
        return response
    except Exception as e:
        return f"Error processing request: {e}"
