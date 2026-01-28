from langchain.tools import Tool

def validate_risk_profile(inputs: dict, result: dict) -> dict:
    score = result.get("total_score")
    category = result.get("risk_category")

    issues = []

    # Simple logical checks
    if inputs.get("investment_horizon", 3) >= 4 and category == "Conservative":
        issues.append("Long investment horizon usually suggests higher risk tolerance.")

    if inputs.get("loss_tolerance", 1) <= 2 and category == "Aggressive":
        issues.append("Low loss tolerance conflicts with aggressive classification.")

    if inputs.get("liquidity_need", 5) >= 4 and category == "Aggressive":
        issues.append("High liquidity needs often reduce risk appetite.")

    if issues:
        return {
            "status": "FLAGGED",
            "issues": issues
        }

    return {
        "status": "VALID",
        "message": "Risk profile is consistent with client responses."
    }

self_validation_tool = Tool(
    name="Risk Profile Validator",
    func=validate_risk_profile,
    description=(
        "Validates whether the calculated risk profile is logically consistent "
        "with the client's input scores."
    )
)
