from langchain.tools import Tool

def map_answer_to_score(question: str, answer: str) -> int:
    answer = answer.lower()

    if "horizon" in question:
        if "short" in answer:
            return 1
        elif "medium" in answer:
            return 3
        else:
            return 5

    if "loss" in question:
        if "panic" in answer or "sell" in answer:
            return 1
        elif "wait" in answer:
            return 3
        else:
            return 5

    if "experience" in question:
        if "new" in answer or "beginner" in answer:
            return 1
        elif "some" in answer:
            return 3
        else:
            return 5

    if "income" in question:
        if "unstable" in answer:
            return 1
        elif "somewhat" in answer:
            return 3
        else:
            return 5

    if "liquidity" in question:
        if "high" in answer:
            return 1
        elif "medium" in answer:
            return 3
        else:
            return 5

    return 3  # safe default

answer_mapper_tool = Tool(
    name="Answer Mapping Tool",
    func=map_answer_to_score,
    description=(
        "Converts a client's natural language answer into a numeric risk score "
        "based on the question context."
    )
)
