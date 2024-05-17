import streamlit as st
from FetchAndTrain import Fetch
import time
#Python Docs
st.set_page_config(
    page_title="Python Docs AI",
    page_icon="📚",
)
st.sidebar.success("Select app")
st.title("Python Docs")




if "message" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Message CodeSolveAI"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role":"User","content":prompt})

# response = type(prompt)
# response = Fetch.FetchAndTrainStackOverFlow(str(prompt))
response = Fetch.PythonOrg(str(prompt))
if response == None:
    response = "Welcome to Python Documentation: CodeSolveAI"
with st.chat_message("assistant"):
    st.markdown(response)
st.session_state.messages.append({"role":"User","content":response})

