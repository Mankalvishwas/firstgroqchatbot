from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

app=FastAPI(
    title="vishwas groqchatbot",
    version="1.0",
    description="A chatbot built using LangChain and Groq's LLM API"
)

llm=ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

Prompt1 =ChatPromptTemplate.from_template(
    "write me an essay on {topic} in 100 words"
)

Prompt2=ChatPromptTemplate.from_template(
    "write me a poem on {topic} in 100 words"
)

add_routes(
    app,
    Prompt1 |llm,
    path="/essay"
)
add_routes(
    app,
    Prompt2 |llm,
    path="/poem"
)
if __name__=="__main__":   
     uvicorn.run(app,host="localhost",port=8000)