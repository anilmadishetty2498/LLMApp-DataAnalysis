# Databricks notebook source
import streamlit as st
from dotenv import load_dotenv
from utility import query_agent
from langchain_groq import ChatGroq

load_dotenv()


st.title("Let's do some analysis on your CSV")
st.header("Please upload your CSV file here:")

# Capture the CSV file
data = st.file_uploader("Upload CSV file",type="csv")
#file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

query = st.text_area("Enter your query")
button = st.button("Generate Response")

if button:
    # Get Response
    answer =  query_agent(data,query)
    st.write(answer)