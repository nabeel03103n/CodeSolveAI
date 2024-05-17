import streamlit as st
import pyttsx3
from FetchAndTrain import Fetch
#Python Docs
st.set_page_config(
    page_title="Wikipedia",
    page_icon="💻",
)
st.sidebar.success("Select app")
st.title("Wikipedia")

engine = pyttsx3.init()
def speak():
    engine.save_to_file(response,"text.mp3")
    engine.runAndWait()
    st.audio("text.mp3")

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
response = "Welcome to Wikipedia: CodeSolveAI"
if prompt == None:
    pass
else:
    response = Fetch.FetchWikipedia(str(prompt))
with st.chat_message("assistant"):
    st.markdown(response)
    # speaker = st.button(label="Speak")
    # if speaker:
st.session_state.messages.append({"role":"User","content":response,"audio":speak()})


