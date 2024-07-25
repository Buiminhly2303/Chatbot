import streamlit as st
import uuid

from conversational_rag import generate_anwser, conversational_rag_chain

# Setting page title and header
st.set_page_config(page_title="Pre-test Qode", page_icon=":robot_face:")

st.title("💬 Customer Support Chatbot ")
st.caption("🚀 A customer support chatbot powered by Ly Bui ")

if "session_id" not in st.session_state:
    st.session_state.session_id = uuid.uuid4()

# Initialise session state variables
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello, Welcom to chatbot automation interview"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = generate_anwser(conversational_rag_chain, prompt, st.session_state.session_id.hex)


    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
