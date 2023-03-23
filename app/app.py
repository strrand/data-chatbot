import openai
import time
import streamlit as st
from dotenv import load_dotenv
import os
import uuid

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv('openai.api_key')

def chat(input_text):
    messages = [
        {"role": "System", "content": "You are a helpful assistant working at LeasePlan Sweden AB and have good knowledge about the leasing business."},
        {"role": "User", "content": input_text},
    ]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Conversation:\n" + '\n'.join([f'{m["content"]}' for m in messages]) + "\n",
        max_tokens=1024,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    messages.append({"role": "Assistant", "content": message})
    return message

def app():
    # Set the title of the app
    st.title("Chatbot")

    # Print a welcome message
    st.write("Hi, I'm a chatbot. What can I help you with today?")

    # Start the conversation
    input_id = uuid.uuid4()
    form_key = uuid.uuid4()
    # Get the user's input
    with st.form(key=str(form_key)):
        user_input = st.text_input("You:", key=input_id)

        # Wait for the user to press the "Enter" key
        if st.form_submit_button(label="Enter"):
            # Exit the conversation if the user says "bye"
            if user_input.lower() == "bye":
                st.write("Chatbot: Goodbye!")
            else:
                # Generate a response using the chat function
                response = chat(user_input)

                # Display the response in a text output widget
                st.write("Chatbot:")
                st.write(response)

# Run the Streamlit app
if __name__ == "__main__":
    app()
