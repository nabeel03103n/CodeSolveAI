import streamlit as st
import numpy as np

st.title("Bot")

if "message" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role":"User","content":prompt})

response = f"Echo:  {prompt}"
with st.chat_message("assistant"):
    st.markdown(response)
st.session_state.messages.append({"role":"User","content":response})
