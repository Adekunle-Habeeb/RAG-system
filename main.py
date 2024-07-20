import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain
import time

st.title("Habeeb's 🚀 Intelligent QA System")
st.write("Welcome to Habeeb's smart query app! :wave:")

st.info(
    """
    You can ask questions about various topics related to Habeeb Adekunle:
    - **Background**: "Who is Habeeb Adekunle?", "What is Habeeb's educational background?"
    - **Technologies Proficient In**: "What technologies is Habeeb proficient in?"
    - **Work Experience**: "What is Habeeb's work experience?"
    - **Projects**: "What are Habeeb's projects in machine learning?", "What are the main features of the temperature prediction model built by Habeeb?"
    - **Languages Spoken**: "What languages can Habeeb Adekunle speak?"
    - **Certifications**: "What certifications does Habeeb Adekunle hold?"
    - **Soft Skills**: "What soft skills does Habeeb Adekunle possess?"

    Feel free to ask any related questions!
    """
)

button = st.button("Start QA Session")

if button:
    create_vector_db()

# Chat-like input for questions
question = st.chat_input("Ask your question here: ")

if question:
    # Display the question in chat format
    st.chat_message("user").write(question)

    # Get the answer from the QA system
    chain = get_qa_chain()
    response = chain({"query": question})


    if isinstance(response, str):
        answer = response

        # Create a placeholder for the answer
        placeholder = st.empty()
        # Split the answer into words
        words = answer.split()

        # Display the answer one word at a time
        display_text = ""
        for word in words:
            display_text += word + " "
            placeholder.markdown(display_text.strip())
            time.sleep(0.05)
    else:
        st.error("The response was not in the expected format.")
else:
    st.info("Please enter a question to get started.")



