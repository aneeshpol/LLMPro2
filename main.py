from database import init_db
from ingest import ingest_rss
import streamlit as st
from dotenv import load_dotenv
from query_agent import read_database
from query_agent import get_llm_response
from query_agent import get_deepseek_response
from prompt import prompt
from rss_links import rss_dictionary
from lang_chain_agent import run_query_agent
load_dotenv()

init_db()

for link in rss_dictionary.values():
    print(link)
    ingest_rss(link)

st.set_page_config(page_title = "NewsAgent")
st.header("NewsAgent: Get news at the click of a button")
question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_deepseek_response(question, prompt)
    #response = run_query_agent(question)
    st.subheader("Related News:")
    #st.code(response, language='sql')
    #full_response = run_query_agent(question)
        
    
    #st.subheader("Response:")
    #st.write(full_response)

    data = read_database(response)
    if data is not None and not data.empty:
        st.subheader("Query Results:")
        st.dataframe(data)
    else:
        st.warning("No results found or query failed.")