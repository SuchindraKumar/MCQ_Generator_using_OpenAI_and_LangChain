import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

# Loading JSON File

with open('Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

# Creating a Title for the App
st.title("MCQs Creator Application with LangChain 🦜⛓️")

# Create a form using st.form
with st.form("user_inputs"):
    # File Upload
    uploaded_file=st.file_uploader("Uplaod a PDF or txt file")

    # Input Fields
    mcq_count=st.number_input("No. of MCQs", min_value=3, max_value=50)

    # Subject
    subject=st.text_input("Insert Subject",max_chars=50)

    # Quiz Tone
    tone=st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

    # Add Button
    button=st.form_submit_button("Create MCQs")

    # Check if the Button is Clicked and All Fields Have Inputs

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)
                # Count Tokens and the Cost of API call
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                        {
                        "text": text,
                        "number": mcq_count,
                        "subject":subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                            }
                    )
                #st.write(response)

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")

            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response, dict):
                    #Extract the Quiz Data from the Response
                    quiz=response.get("quiz", None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.columns = ["Question", "Options", "Correct Answer"]
                            df.index=df.index+1
                            st.table(df)
                            # Display the Review in a Text Box as well
                            st.text_area(label="Review", value=response["review"])
                            # Add download button
                            csv = df.to_csv(index=False)
                            st.download_button(
                                label="Download CSV",
                                data=csv,
                                file_name='generated_mcqs.csv',
                                mime='text/csv')
                        else:
                            st.error("Error in the Table Data")

                else:
                    st.write(response)