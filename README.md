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
        else
        category = "Aggressive"
Project structure

client-risk-agent/
│
├── README.md
├── requirements.txt
├── .env
│
├── main.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── agents/
│   ├── __init__.py
│   └── risk_agent.py
│
├── tools/
│   ├── __init__.py
│   └── risk_scoring.py
│
├── prompts/
│   ├── __init__.py
│   └── risk_profile_prompt.py
│
├── memory/
│   ├── __init__.py
│   └── memory_store.py
│
└── data/
    └── sample_client.json
