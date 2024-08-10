import streamlit as st
import pypdf
from langchain.llms import Anthropic
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Function to process uploaded resumes
def process_resume(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        reader = pypdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    elif uploaded_file.name.endswith('.txt'):
        return uploaded_file.getvalue().decode("utf-8")
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or TXT file.")

# Function to create QA chain
def create_qa_chain(text):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(text)
    
    embeddings = HuggingFaceEmbeddings()
    
    db = FAISS.from_texts(texts, embeddings)
    retriever = db.as_retriever()
    
    template = """You are an AI assistant for HR professionals analyzing resumes. 
    Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    {context}

    Question: {question}
    Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template=template,
    )

    llm = Anthropic(model="claude-2", anthropic_api_key=st.secrets["anthropic_api_key"])
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        return_source_documents=True
    )
    return qa_chain

# Streamlit app
def main():
    st.title("Resume Analysis Assistant for HR")

    # File upload
    uploaded_file = st.file_uploader("Upload a resume (PDF or TXT)", type=["pdf", "txt"])

    if uploaded_file is not None:
        # Process the resume
        with st.spinner("Processing resume..."):
            try:
                text = process_resume(uploaded_file)
                qa_chain = create_qa_chain(text)
                st.success("Resume processed successfully!")
            except Exception as e:
                st.error(f"Error processing resume: {str(e)}")
                return

        # Predefined questions
        predefined_questions = [
            "What are the candidate's key skills?",
            "Summarize the candidate's work experience.",
            "What is the candidate's educational background?",
            "Does the candidate have experience with project management?",
            "What programming languages does the candidate know?",
            "Summarize the candidate's qualifications for a software developer role."
        ]

        # Question input
        question = st.selectbox(
            "Select a question or type your own:",
            [""] + predefined_questions
        )
        custom_question = st.text_input("Or ask your own question:")

        if question or custom_question:
            with st.spinner("Analyzing..."):
                try:
                    result = qa_chain({"query": question or custom_question})
                    st.write("Answer:", result['result'])
                except Exception as e:
                    st.error(f"Error analyzing resume: {str(e)}")
                    return

            # Confidence score (this is a placeholder - actual implementation would depend on the model's capabilities)
            confidence = st.slider("How confident are you in this answer?", 0, 100, 50)

            # Feedback
            feedback = st.radio("Was this answer helpful?", ("Yes", "No"))
            if feedback == "No":
                st.write("Thank you for your feedback. We'll work on improving our responses.")
                improvement_suggestion = st.text_area("Please suggest how we could improve:")
                if improvement_suggestion:
                    st.write("Thank you for your suggestion. We'll take it into account for future improvements.")

if __name__ == "__main__":
    main()