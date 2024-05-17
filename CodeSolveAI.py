import streamlit as st
from FetchAndTrain import Fetch
import time
#StackOverFlow
st.set_page_config(
    page_title="CodeSolveAI",
    page_icon="🤖",
)
st.sidebar.success("Select app")
st.title("CodeSolveAI")




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
response = Fetch.FetchAndTrainStackOverFlow(str(prompt))
if prompt == None:response = "Welcome to CodeSolveAI : Ready to use"
with st.chat_message("assistant"):
    st.markdown(response)
st.session_state.messages.append({"role":"User","content":response})

