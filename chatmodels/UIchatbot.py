import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Initialize model
model = ChatMistralAI(model="mistral-small-2506")

# Page config
st.set_page_config(page_title="AI Mood Chatbot", page_icon="🤖", layout="centered")

# Custom CSS for aesthetics
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
    }
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Mood Chatbot")
st.subheader("Choose how your AI behaves 👇")

# Mode selection
mode_option = st.radio(
    "Select AI Mode:",
    ("😡 Angry", "😂 Funny", "😢 Sad")
)

# Map modes
if mode_option == "😡 Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_option == "😂 Funny":
    mode = "You are very funny AI agent. You respond with humor and jokes."
else:
    mode = "You are very sad AI agent. You respond with sadness and tiredness as you are depressed."

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]
    st.session_state.mode = mode

# Reset chat if mode changes
if st.session_state.mode != mode:
    st.session_state.messages = [SystemMessage(content=mode)]
    st.session_state.mode = mode

st.divider()

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# Chat input
prompt = st.chat_input("Type your message... (0 to exit)")

if prompt:
    if prompt == "0":
        st.stop()

    # Add user message
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    # Get response
    response = model.invoke(st.session_state.messages)

    # Add AI response
    st.session_state.messages.append(AIMessage(content=response.content))
    st.chat_message("assistant").write(response.content)
