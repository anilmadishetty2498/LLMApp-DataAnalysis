# Databricks notebook source
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from langchain import HuggingFaceHub
import pandas as pd
#from langchain.llms import OpenAI
import os
from langchain_groq import ChatGroq


def query_agent(data, query):

    # Parse the CSV file and create a Pandas DataFrame from its contents.
    df = pd.read_csv(data)

    #llm = OpenAI()
    #llm = HuggingFaceHub(repo_id = "google/flan-t5-large")
    #llm = ChatGroq(groq_api_key = groq_api_key, model_name = "mixtral-8x7b-32768", temperature=1)

    llm = ChatGroq(model_name = "mixtral-8x7b-32768", temperature=1)
    
    # Create a Pandas DataFrame agent.
    #agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)
    agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True, agent_type="openai-tools")

    #Python REPL: A Python shell used to evaluating and executing Python commands. 
    #It takes python code as input and outputs the result. The input python code can be generated from another tool in the LangChain
    return agent.invoke(query)

# COMMAND ----------