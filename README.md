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


 HOW TO RUN
 pip install -r requirements.txt
 python main.py



Make a note that :
the app separates reasoning from decision logic.
The LLM understands language, but the final scoring is deterministic and auditable

Further
Since we are relying on self-validation step, this undermines autonomy, reasoning, and responsibility which are all very banking-aligned principles.
This is just a sanity check on client's responses
After the agent calculates the risk profile, it will:

Review the inputs

Review the final risk category

Ask itself:

“Does this classification logically align with the client’s responses?”

Either:

✅ Confirm the result

For example, Although your total score suggests an Aggressive profile, if your tool find a low tolerance for losses :it marks as a conflict.
This case then gets flagged for advisor review

⚠️ Flag an inconsistency and explain it
