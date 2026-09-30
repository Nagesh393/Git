import pandas as pd 
import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}!")
num=st.slider("Pick number", 0,100)

st.sidebar.title("Settings")






st.warning("Please check your input.")
st.error("Something went wrong.")

st.info("Processing your data...")
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = "AI response will go here..."
        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
