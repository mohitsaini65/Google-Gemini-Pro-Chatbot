import streamlit as st
import google.generativeai as genai

st.title("My First Chatbot 🤖")

# Get API key from Streamlit Secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Store chat messages
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
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)

    with st.chat_message("assistant"):
        st.write(response.text)

    st.session_state.messages.append(
        {"role": "assistant", "content": response.text}
    )
