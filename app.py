import os
import streamlit as st

from dotenv import load_dotenv
from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from langchain_groq import ChatGroq

from PIL import Image

logo = Image.open("assets/logo.png")

col1, col2 = st.columns([1, 6])

with col1:
    st.image(logo, width=80)

with col2:
    st.markdown("""
    <h1 style='color:#38bdf8;margin-bottom:0px;'>
        AI PDF Chatbot
    </h1>

    <h4 style='color:#cbd5e1;'>
        Chat with your PDF using
        <span style='color:#22c55e;'>Gemini Embeddings</span> +
        <span style='color:#f97316;'>Groq Llama</span>
    </h4>
    """, unsafe_allow_html=True)

st.divider()

# -----------------------------
# Load Environment Variables
# -----------------------------

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("Google Key:", GOOGLE_API_KEY[:10] if GOOGLE_API_KEY else "Not Found")
print("Groq Key:", GROQ_API_KEY[:10] if GROQ_API_KEY else "Not Found")

EMBEDDING_MODEL = "models/gemini-embedding-001"
FAISS_PATH = "faiss_index"


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="📄",
    layout="wide"
)

with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Extract Text from PDF
# -----------------------------

def extract_pdf_text(pdf_files):

    text = ""

    for pdf in pdf_files:

        try:
            reader = PdfReader(pdf)

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        except Exception as e:

            st.error(f"Error reading {pdf.name}: {e}")

    return text


# -----------------------------
# Split Text into Chunks
# -----------------------------

def split_text(text):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,
        chunk_overlap=200

    )

    return splitter.split_text(text)


# -----------------------------
# Create FAISS Vector Store
# -----------------------------

def create_vector_store(chunks):

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL
    )

    vector_store = FAISS.from_texts(

        texts=chunks,
        embedding=embeddings

    )

    vector_store.save_local(FAISS_PATH)
    
def get_answer(user_question):

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL
    )

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(
        search_kwargs={"k": 4}
    )

    prompt_template = PromptTemplate.from_template("""
Answer the question using only the provided context.

If the answer is not available in the context, reply:

"Answer is not available in the uploaded PDF."

Context:
{context}

Question:
{question}

Answer:
""")

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

    chain = (
        RunnableParallel(
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
        )
        | prompt_template
        | llm
        | StrOutputParser()
    )

    return chain.invoke(user_question)

# -----------------------------
# Main Function
# -----------------------------

def main():

    # -----------------------------
    # Question Box
    # -----------------------------
    st.markdown("### 💬 Ask a question")

    user_question = st.text_input(
        "",
        placeholder="Ask anything about your uploaded PDF..."
    )

    if user_question:

        answer = get_answer(user_question)

        st.session_state.messages.append(
        {
            "question": user_question,
            "answer": answer
        }
    )
        if st.session_state.messages:

            st.markdown("## 💬 Chat History")

            for chat in reversed(st.session_state.messages):

                with st.container(border=True):

                    st.markdown(f"**👤 You:** {chat['question']}")

                    st.markdown("---")

                    st.markdown(f"**🤖 AI:** {chat['answer']}")
    # -----------------------------
    # Sidebar
    # -----------------------------
    with st.sidebar:

        st.markdown("## 📂 Upload PDF")
        st.markdown(
            "<p style='color:#cbd5e1;'>Upload one or more PDF files to start chatting.</p>",
            unsafe_allow_html=True,
        )

        pdf_docs = st.file_uploader(
            "Choose PDF files",
            accept_multiple_files=True,
            type=["pdf"]
        )

        if st.button("🚀 Process PDF"):

            if pdf_docs:

                with st.spinner("Processing PDF..."):

                    raw_text = extract_pdf_text(pdf_docs)
                    text_chunks = split_text(raw_text)
                    create_vector_store(text_chunks)

                st.success("✅ PDF processed successfully!")

            else:
                st.warning("Please upload at least one PDF.")

        if st.button("🗑 Clear History"):
            st.session_state.messages = []
            st.rerun()


# -----------------------------
# Run App
# -----------------------------

if __name__ == "__main__":
    main()