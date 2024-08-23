import os
from dotenv import load_dotenv
from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings

load_dotenv()


llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0)

instructor_embeddings = HuggingFaceInstructEmbeddings()
vectordb_file_path = 'faiss_index'

def create_vector_db():
    loader = CSVLoader(file_path='about_habeeb.csv', source_column='Question')
    data = loader.load()
    vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)
    
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making many changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.
    If the question is a greeting like "Hello" or "Hi," respond with a generic greeting.

    CONTEXT: {context}

    QUESTION: {question}"""


    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=['context', 'question']
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=retriever,
        input_key='query',
        return_source_documents=True,
        chain_type_kwargs={'prompt': PROMPT}
    )

    # def get_answer(question):
    #     response = chain(question)
    #     return response["result"]

    def get_answer(question):
        greetings = ["hello", "hi", "hey"]
        if isinstance(question, str) and question.lower() in greetings:
            return "Hi there! How can I assist you today?"
        response = chain(question)
        
        print("Retrieved Context:", response["source_documents"])
        return response["result"]



    return get_answer

if __name__ == '__main__':
    create_vector_db()
    get_answer = get_qa_chain()
    print(get_answer('What work experience does Habeeb have?'))
