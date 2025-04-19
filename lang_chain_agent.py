from langchain_community.utilities import SQLDatabase

from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_cohere.sql_agent.agent import create_sql_agent
import re
from prompt import custom_prompt
from openai import OpenAI
import os



db_url = SQLDatabase.from_uri(os.getenv("DATABASE_URL"))


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY2"),
    base_url="https://openrouter.ai/api/v1",
    )

llm = ChatOpenAI(
    temperature=0.2,
    model="deepseek/deepseek-chat-v3-0324:free",
    openai_api_key=os.getenv("OPENROUTER_API_KEY2"),
    openai_api_base="https://openrouter.ai/api/v1"
)

toolkit = SQLDatabaseToolkit(db=db_url, llm=llm)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    #verbose=True,  
      
    handle_parsing_errors=True
)

def run_query_agent(user_input: str) -> str:
    try:
        response = agent_executor.invoke(user_input) 
        return response
    except Exception as e:
        return f"Error: {str(e)}"