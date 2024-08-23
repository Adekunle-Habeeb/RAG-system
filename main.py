import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain
import time

st.title("Habeeb's 🚀 Intelligent QA System")
st.write("Welcome to Habeeb's smart query app! :wave:")

st.info(
    """
    You can ask questions about various topics related to Habeeb Adekunle:
    - **Background**: "Who is Habeeb Adekunle?", "What is Habeeb's educational background?"
    - **Technologies Proficient In**: "What technologies is Habeeb proficient in?", "What AI tools and frameworks does Habeeb use?"
    - **Work Experience**: "What is Habeeb's work experience?", "What roles has Habeeb held in backend and machine learning engineering?"
    - **Projects**: "What are Habeeb's projects in machine learning?", "Can you describe Habeeb's temperature prediction model?", "What are some of Habeeb's notable AI applications?"
    - **Languages Spoken**: "What languages can Habeeb Adekunle speak?"
    - **Soft Skills**: "What soft skills does Habeeb Adekunle possess?", "How does Habeeb approach problem-solving and teamwork?"

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



