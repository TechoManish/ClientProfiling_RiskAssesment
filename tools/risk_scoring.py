from langchain.tools import Tool

def calculate_risk_score(profile: dict) -> dict:
    score = sum(profile.values())

    if score <= 12:
        category = "Conservative"
    elif score <= 20:
        category = "Balanced"
    else:
        category = "Aggressive"

    return {
        "total_score": score,
        "risk_category": category
    }

risk_scoring_tool = Tool(
    name="Risk Scoring Tool",
    func=calculate_risk_score,
    description=(
        "Calculates client's risk profile based on numeric inputs. "
        "Input must be a dictionary with risk factors as integers."
    )
)
