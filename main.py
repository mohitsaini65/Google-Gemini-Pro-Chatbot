import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="My First Chatbot 🤖")
st.title("My First Chatbot 🤖")

# Get token from Streamlit secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

# Create client
client = InferenceClient(token=HF_TOKEN)

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
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.write(user_input)

    # ✅ CHAT COMPLETION (WORKING)
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

        st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

