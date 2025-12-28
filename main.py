import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="My First Chatbot 🤖")
st.title("My First Chatbot 🤖")

# Get token from Streamlit Secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

# Create Hugging Face client
client = InferenceClient(token=HF_TOKEN)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.write(user_input)

    # Generate AI response (WORKING METHOD)
    response = client.chat_completion(
        model="HuggingFaceH4/zephyr-7b-beta",
        messages=[
            {"role": "user", "content": user_input}
        ],
        max_tokens=200
    )

    reply = response.choices[0].message["content"]

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

