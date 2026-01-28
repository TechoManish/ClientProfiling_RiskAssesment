from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from tools.risk_scoring import risk_scoring_tool
from prompts.risk_profile_prompt import SYSTEM_PROMPT

def run_risk_agent():
    llm = ChatOpenAI(
        temperature=0.3,
        model="gpt-4o-mini"
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    tools = [risk_scoring_tool]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        system_message=SYSTEM_PROMPT
    )

    while True:
        user_input = input("\nClient: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = agent.run(user_input)
        print(f"\nAgent: {response}")
