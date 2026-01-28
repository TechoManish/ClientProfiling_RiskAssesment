# ClientProfiling_RiskAssesment
Client Profiling &amp; Risk Assessment Agent in Wealth Investment

User
 ↓
LLM (ChatOpenAI)
 ↓
Agent (Reasoning)
 ↓
Tools
 ├─ Risk Scoring Tool (Python)
 └─ Profile Storage (Memory)
 ↓
Final Risk Profile + Explanation

#AgentType.ZERO_SHOT_REACT_DESCRIPTION

 if score <= 12:
        category = "Conservative"
    elif score <= 20:
        category = "Balanced"
    else:
        category = "Aggressive"
