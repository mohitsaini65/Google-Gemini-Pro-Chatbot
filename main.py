import streamlit as st
from groq import Groq

st.title("My First Chatbot 🤖")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

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

    # ✅ NEW GROQ API (CORRECT)
    response = client.responses.create(
        model="llama3-8b-8192",
        input=user_input,
        max_output_tokens=512
    )

    reply = response.output_text

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )









