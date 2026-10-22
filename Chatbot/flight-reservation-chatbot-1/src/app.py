import streamlit as st
from chatbot.intents import Intents
from chatbot.responses import Responses

def main():
    st.title("Flight Reservation Chatbot")
    st.write("Welcome to the Flight Reservation Chatbot! How can I assist you today?")

    intents = Intents()
    responses = Responses()

    user_input = st.text_input("You: ", "")
    
    if user_input:
        intent = intents.get_intent(user_input)
        response = responses.get_response(intent)
        st.write(f"Bot: {response}")

if __name__ == "__main__":
    main()