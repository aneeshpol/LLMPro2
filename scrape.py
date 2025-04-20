import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
llm = ChatOpenAI(
    temperature=0.2,
    model="deepseek-ai/deepseek-chat",
    openai_api_key=os.getenv("OPENROUTER_API_KEY2"),
    openai_api_base="https://openrouter.ai/api/v1"
)


def scrape_website(website):
    print("Launching chrome browser")
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service = Service(chrome_driver_path), options= options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    else:
        return""
    
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for sos in soup(["script", "style"]):
        sos.extract()
    cc = soup.get_text(separator="\n")
    cc = "\n".join(line.strip() for line in cc.splitlines() if line.strip())
    return cc

def split_dom_content(dom_content, max_length= 6000):
    return [ dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)] 

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_desc}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parser(dom_chunks, parse_desc):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm
    results = []

    for i, chunk in enumerate(dom_chunks, start = 1 ):
        response = chain.invoke({"dom_content": chunk, "parse_desc": parse_desc })
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        results.append(response)
    return "/n".join(results)


def scraping_df(link_number, data):
    link = data.iloc[link_number, 2]
    
    return(link)