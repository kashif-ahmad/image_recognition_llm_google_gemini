# load dotenv for programming
from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

# import files
import streamlit as st
import os
import google.generativeai as genai

# configure the Google API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Load Gemeni Pro model and get responses
model=genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_model_response(question):
    response = chat.send_message(question,stream=True)
    return response

## initialize streamlit app
st.set_page_config(page_title="Chat History App")
st.header("Chat history App with Gemini")

if 'bot_history' and 'my_history' not in st.session_state:
    st.session_state['bot_history'] = ''
    st.session_state['my_history'] = ''

input   = st.text_input("Input: ", key="input")
submit  = st.button("Ask Question")

if submit and input:
    response=get_model_response(input)

    ## add user query and model response into history
    st.session_state['my_history'] = st.session_state['my_history'] + input + '\n'
    st.subheader("The response is")

    for chunk in response:
        st.write(chunk.text)
        st.session_state['bot_history'] = st.session_state['bot_history'] + chunk.text

    st.session_state['bot_history'] = st.session_state['bot_history'] + '\n'

st.subheader("The chat history is")

st.write (f"{st.session_state['bot_history']}" + '\n')
st.write (f"{st.session_state['my_history']}" + '\n')

