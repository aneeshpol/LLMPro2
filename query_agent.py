from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from openai import OpenAI
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    )

db_url = os.getenv("DATABASE_URL")

#genai.configure(api_key = os.getenv("GOOGLE_KEY"))

def get_llm_response(question, prompt):
    model = genai.GenerativeModel(model_name="models/gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text

def get_deepseek_response(question: str, prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ],
            temperature=0.2,
            max_tokens=512
        )
        if not response or not response.choices:
           return "No valid response received from DeepSeek."
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error : {str(e)}"

def read_database(sql_query: str, db_url: str = db_url):
    try:
        engine = create_engine(db_url)
        with engine.connect() as connection:
            result = connection.execute(text(sql_query))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            return df
    except Exception as e:
        st.error(f"Database error: {e}")
        return None
    













