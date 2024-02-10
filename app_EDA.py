import streamlit as st
import pandas as pd
# from langchain_community.llms import OpenAI
# from langchain_experimental.agents import create_pandas_dataframe_agent
# from langchain.agents import create_pandas_dataframe_agent
# from langchain_openai import ChatOpenAI
# from langchain_openai import OpenAI

from openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents.agent_toolkits import create_pandas_dataframe_agent
from dotenv import find_dotenv
from config2 import set_environment
set_environment()


# llm model
llm = OpenAI(temperature=0,)

# Streamlit user interface

# Main

st.title("AI Assistant for Data Science 🤖")
st.write("Hi there 👋. I am your AI assistant. I will offer solutions based on Exploratory Data Analysis (EDA) problem.")


with st.sidebar:
    st.write("*Unleash the power of AI in your business with our AI Assistant!*")
    st.caption("""**Unleash the power of AI in your business with our AI Assistant! 
             Just upload a CSV file, and watch as it transforms complex data into actionable insights. 
             Harnessing the latest in machine learning, this Assistant isn't just a tool, it's your strategic partner, 
             ready to propel your business decisions into a new realm of efficiency and accuracy. 
             Welcome to the future of data analysis, where every decision is data-driven and every 
             insight is a step towards success.** 🚀🤖💼""")
    
    with st.expander("EDA steps"):
        st.write(llm("What the steps of a simple EDA?"))

    st.divider()

    st.caption("<p style='text-align: center'>with love from SisengAI.com </p>", unsafe_allow_html=True)

# Initialize the key in session state
if "clicked" not in st.session_state:
    st.session_state.clicked = {1:False}

# Function to update the value in session state
def clicked(button):
    st.session_state.clicked[button] = True
st.button("Lets get started!", on_click=clicked, args=[1])

if st.session_state.clicked[1]:
    st.header("Exploratory Data Analysis (EDA)")
    st.subheader("Solution")

    user_csv = st.file_uploader("Upload your CSV file", type=["csv"])

    if user_csv is not None:
        user_csv.seek(0)
        df = pd.read_csv(user_csv, low_memory=False)

with st.sidebar:
    with st.expander("EDA steps"):
        st.write(llm("What the steps of a simple EDA?"))



try:
    pandas_agent = create_pandas_dataframe_agent(
        llm, 
        df, 
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        )
    # Consider a more basic question for now
    question = "Describe the columns in the dataset." 
    col_descriptions = pandas_agent.run(question)
    st.write(col_descriptions)
except Exception as e:
    st.error("An error occurred while processing your request. Please check your CSV file and try again. Here's some technical info: {}".format(e))

