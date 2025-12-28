import streamlit as st
from huggingface_hub import InferenceClient

# Page title
st.set_page_config(page_title="My First Chatbot 🤖")
st.title("My First Chatbot 🤖")

# Get token from Streamlit Secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

# Hugging Face client (THIS MODEL WORKS)
client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=HF_TOKEN
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # AI response
    with st.chat_message("assistant"):
        response = client.text_generation(
            prompt=user_input,
            max_new_tokens=200,
            temperature=0.7
        )
        st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})







