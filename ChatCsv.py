from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai
import pandas as pd

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


st.set_page_config(page_title="ChatCsv")
st.header("Chat with CSV")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'])

if input_csv is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("CSV Uploaded Successfully")
        data = pd.read_csv(input_csv)
        st.dataframe(data, use_container_width=True)

    with col2:
        st.info("Chat Below")
        input_prompt = st.text_input("Input: ", key="input")
        submit = st.button("Ask the question")

        if submit and input_prompt:

            question = data.to_string(index=False) + "\n" + input_prompt
            response = get_gemini_response(question)


            st.subheader("The Response:")
            for chunk in response:
                st.write(chunk.text)
