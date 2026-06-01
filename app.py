from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant,answers the user questions with acurate and concise information. If you don't know the answer, say you don't know."),
    ("user","{question}")
])

output_parser=StrOutputParser()
chain=prompt|llm|output_parser

st.title("vishwas groqchatbot ")
input_text=st.text_input("i am groq your personal chatbot,please ask me the questions")

if input_text:
    response=chain.invoke({"question":input_text})
    st.write(response)