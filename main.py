import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="My First Chatbot 🤖")
st.title("My First Chatbot 🤖")

HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.write(user_input)

    response = client.text_generation(
        user_input,
        max_new_tokens=150,
        temperature=0.7
    )

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )


