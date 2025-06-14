import streamlit as st
import google.generativeai as genai

genai.configure(api_key='API_KEY')
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="AI CHATBOT")
st.title("My Gemini Chatbot") 

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role":"assistant", "content": "你好，請問我要如何幫助你?"}]
    st.hist = []


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    if msg["role"] == "assistant":
        st.hist.append({"role": "model", "parts": [ {"text": msg["content"]}] })
    else:
        st.hist.append({"role": msg["role"], "parts": [ {"text": msg["content"]}] })
    #TODO


if prompt := st.chat_input("請輸入訊息"):

    st.session_state.messages.append({"role":"user" ,"content": prompt})
    st.chat_message("user").write(prompt)

    #TODO

    #TODO
    st.chat_message("assistant").write("TODO")
    st.session_state.messages.append({"role":"assistant", "content": "TODO"})

