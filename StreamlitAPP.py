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
with open("D:\Projects\MCQ_Genrator_using_OpenAI_and_LangChain\Response.json","r") as file:
    RESPONSE_JSON = json.load(file)

# Creating a tital for the app
    st.title("MCQs Creator Application with LnagChain")

# Create a form using st.form
with st.form("user_input"):
    # File Upload
    uploaded_file=st.file_uploader("Upload a PDF or txt File")

    # Input Fields
    mcq_count=st.number_input("No. of MCQs",min_value=3,max_value=50)

    # Subject
    subject=st.text_input("Insert Subject",max_chars=20)

    # Quiz Tone
    tone=st.text_input("Complexity Level of Questions",max_chars=20,placeholder="simple")

    # Add Button
    button=st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading...."):
            try:
                text=read_file(uploaded_file)
                # Count Tokens and Cost of API Call
                with get_openai_callback as cb:
                    response=generate_evaluate_chain(
                        {
                            "text":text,
                            "number":mcq_count,
                            "subject":subject,
                            "tone":tone,
                            "response_json":json.dumps(RESPONSE_JSON)
                        }
                    )
                #st.write(response)

            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")


            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response,dict):
                    # Extract The Quiz Data From The Response
                    quiz=response.get("quiz",None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            # Display the Review in a Text Box as well
                        else:
                            st.error("Error In The Table Data")

                    else:
                        st.write(response)                           




