import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

st.title("LLM sin contexto")
api_key = st.text_input("Enter your Google API Key:", type="password", key="api_key_input")


def generate_response(input_text):
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=api_key)
    parser = StrOutputParser()
    chain = model |parser
    st.write(chain.invoke(input_text))
   
    
   

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "Who is Donald Trump?",
    )
    submitted = st.form_submit_button("Submit")
    if not api_key:
        st.warning("Please enter your API key!", icon="⚠")
    if submitted and api_key:
        generate_response(text)
