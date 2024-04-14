import streamlit as st
import keyboard
from FetchAndTrain import Fetch

st.markdown('''<h1 style='text-align:center;color:white;'>CodeSolveAI</h1>''',unsafe_allow_html=True)

def text():
    st.text(Fetch.FetchAndTrainStackOverFlow(user_input))

user_input = st.text_input(label="Enter")
if st.button("click"):
    text()

if keyboard.is_pressed('enter'):
    text()
