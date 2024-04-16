from llama_cpp import Llama
import time
import streamlit as st

model_path = "D:\TEST\PYTHON\llama models\Llama-2-7B-Chat-GGUF\llama-2-7b-chat.Q4_K_M.gguf"
#For short response
LLM = Llama(model_path=model_path)
#For long response
# LLM = Llama(model_path=model_path,n_ctx=2048)


st.title("Chat Bot AI")

if "message" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Message chat bot..."):
    time_start = time.time()
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role":"User","content":prompt})
    if "show_widget" not in st.session_state:
        st.session_state.show_widget = True
        
    if st.session_state.show_widget:
        st.write("Generating Response...")

    # response = type(prompt)
    #For short response
    response = LLM(prompt,max_tokens=25)
    #For long response
    # response = LLM(prompt,max_tokens=0)
    # print(output["choices"][0]["text"])
    with st.chat_message("assistant"):
        st.markdown(response["choices"][0]["text"])
    st.session_state.messages.append({"role":"User","content":response})
    time_end = time.time()
    st.write(f"Time Taken {int(time_end-time_start)} seconds")

    st.session_state.show_widget = not st.session_state.show_widget
