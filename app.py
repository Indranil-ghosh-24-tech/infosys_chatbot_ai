import streamlit as st
import requests

def send_message(user_message):
    response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json={"sender": "user", "message": user_message}
    )
    return response.json()

st.title("Chatbot")
user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        responses = send_message(user_input)
        for r in responses:
            st.write(f"Bot: {r['text']}")
