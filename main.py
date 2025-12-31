import streamlit as st
from google import genai

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="My First Chatbot", page_icon="🤖")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.stApp {
    background-color: #f7f8fa;
}

h1 {
    text-align: center;
    font-weight: 700;
}

.chat-user {
    background-color: #dcf8c6;
    padding: 12px 15px;
    border-radius: 15px;
    margin: 8px 0;
    text-align: right;
}

.chat-bot {
    background-color: #ffffff;
    padding: 12px 15px;
    border-radius: 15px;
    margin: 8px 0;
    text-align: left;
    border: 1px solid #e6e6e6;
}

textarea {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🤖 My First Chatbot")

# ---------- GEMINI CLIENT ----------
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# ---------- STEP 3: CHAT MEMORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- DISPLAY CHAT HISTORY ----------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div class='chat-user'>{msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='chat-bot'>{msg['content']}</div>",
            unsafe_allow_html=True
        )

# ---------- INPUT ----------
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Gemini response
    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=user_input
    )

    bot_reply = response.text

    # Save bot message
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    st.rerun()


