import streamlit as st
import os
from google.cloud import dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json" 
PROJECT_ID = "customersupport-chatbot-vdek"  
SESSION_ID = "streamlit-session"
LANGUAGE_CODE = "en"

def get_chatbot_response(user_input):
    """Send user input to Dialogflow and return response + parameters."""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, SESSION_ID)

    text_input = dialogflow.types.TextInput(text=user_input, language_code=LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)

    reply = response.query_result.fulfillment_text

    parameters = dict(response.query_result.parameters)

    return reply, parameters

st.set_page_config(page_title="Customer Support Chatbot", layout="centered")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #74ABE2, #5563DE);
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: rgba(255,255,255,0.9);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    }
    .stChatMessage {
        margin: 0.5rem 0;
    }
    .stChatMessage[data-testid="stChatMessage-user"] {
        background-color: #DCF8C6;
        border-radius: 15px;
        padding: 10px 15px;
        color: black;
        max-width: 75%;
        align-self: flex-end;
    }
    .stChatMessage[data-testid="stChatMessage-assistant"] {
        background-color: #F1F0F0;
        border-radius: 15px;
        padding: 10px 15px;
        color: black;
        max-width: 75%;
        align-self: flex-start;
    }
    .stTextInput input {
        border-radius: 20px !important;
        padding: 10px 20px !important;
        border: 1px solid #ccc !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #fff;'>🤖 Customer Support Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #fff;'>Ask me about your order, technical issues, or contact support.</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "👋 Hi! How can I assist you today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    reply, parameters = get_chatbot_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(reply)
        if parameters:
            st.markdown("**Extracted Info:**")
            for key, value in parameters.items():
                if value:  
                    st.markdown(f"- `{key}` → **{value}**")

    st.session_state.messages.append({"role": "assistant", "content": reply})
