from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemeni Pro model and get responses

model=genai.GenerativeModel('gemini-pro')
def get_gemini_response (question):
    response = model.generate_content(question)
    return response.text


## initialize streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

## when submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)



