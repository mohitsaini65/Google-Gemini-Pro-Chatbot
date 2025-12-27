import streamlit as st
from google import genai

st.title("My First Chatbot 🤖")

# Load API key from Streamlit Secrets
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
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

    # Gemini response
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=user_input
    )

    reply = response.text

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )




