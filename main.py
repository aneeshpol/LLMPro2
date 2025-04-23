from database import init_db
from ingest import ingest_rss
import streamlit as st
from dotenv import load_dotenv
from query_agent import read_database
from query_agent import get_deepseek_response
from prompt import prompt
from rss_links import rss_dictionary
from lang_chain_agent import run_query_agent
from scrape import scraping_df
from controller import Controller
load_dotenv()

init_db()

for link in rss_dictionary.values():
    print(link)
    ingest_rss(link)

st.set_page_config(page_title = "NewsAgent")
st.header("NewsAgent: Get news at the click of a button")

if "response" not in st.session_state:
    st.session_state.response = None

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question", "submitbutton")

if submit:
    response = get_deepseek_response(question, prompt)
    st.session_state.response = response

if st.session_state.response:

    
    data = read_database(st.session_state.response)

    if data is not None and not data.empty:

        st.subheader("Related News:")
        st.dataframe(data)

        st.subheader("Enter number to scrape the link")
        link_number=st.text_input("enter link number", key="input2")

        enter = st.button("Ask the question", key = "linkbutton")
        if enter:           
            summary = Controller.get_link(link_number, data)
            st.write(summary)

        else:
            st.error("Please enter a valid numeric index.")
    else:
        st.warning("No results found or query failed.")


