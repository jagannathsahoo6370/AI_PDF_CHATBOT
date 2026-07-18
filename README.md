# 📄 AI PDF Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-orange?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge&logo=google)
![Groq](https://img.shields.io/badge/Groq-Llama-purple?style=for-the-badge)

### 🚀 Chat with your PDF using AI

Upload PDF documents and ask natural language questions to receive intelligent, context-aware answers powered by **Retrieval-Augmented Generation (RAG)**.

</div>

---

# 📸 Application Preview

<p align="center">
### APP Logo

<img src="<<img width="1254" height="1254" alt="logo" src="https://github.com/user-attachments/assets/a37e94e6-e402-4197-a953-1399bfb80a84" />
>"width="100%">

</p>

---

# ✨ Features

- 📂 Upload one or multiple PDF documents
- 📖 Automatic PDF text extraction
- ✂ Smart text chunking using LangChain
- 🧠 Google Gemini Embeddings
- ⚡ FAISS Vector Database
- 🤖 Groq Llama 3.1 LLM
- 💬 Context-aware Question Answering
- 🌙 Modern Dark UI
- 📝 Chat History
- 🚀 Fast Semantic Search
- 🔒 Secure API Key Management using `.env`

---

# 🏗 Project Architecture

```
                PDF Files
                    │
                    ▼
         PyPDF2 Text Extraction
                    │
                    ▼
      RecursiveCharacterTextSplitter
                    │
                    ▼
     Google Gemini Embeddings
                    │
                    ▼
        FAISS Vector Database
                    │
                    ▼
            Similar Chunks
                    │
                    ▼
          Groq Llama 3.1 Model
                    │
                    ▼
             Intelligent Answer
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| PyPDF2 | PDF Reader |
| LangChain | RAG Pipeline |
| Gemini Embeddings | Text Embeddings |
| Groq Llama 3.1 | Large Language Model |
| FAISS | Vector Database |
| Python Dotenv | API Key Management |

---

# 📂 Project Structure

```
AI_PDF_Chatbot
│
├── assets/
│   └── logo.png
│
├── faiss_index/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── app_screenshot.png
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/jagannathsahoo6370/AI_PDF_Chatbot.git
```

```bash
cd AI_PDF_Chatbot
```

---

## Create Virtual Environment

```bash
py -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

---

## Install Requirements

```bash
py -m pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# ▶ Run the Application

```bash
streamlit run app.py
```

---

# 💡 How It Works

1. Upload one or more PDF files.
2. Click **Process PDF**.
3. The application extracts text from the PDFs.
4. Text is divided into semantic chunks.
5. Gemini generates vector embeddings.
6. FAISS stores the embeddings.
7. Ask any question related to your PDF.
8. The chatbot retrieves the most relevant content.
9. Groq Llama generates an accurate answer.

---

# 📌 Future Improvements

- 📚 Multiple Chat Sessions
- 📄 PDF Summarization
- 🌐 Multi-language Support
- 🔊 Voice Input
- 📥 Export Chat History
- ☁ Deploy on Streamlit Cloud
- 🧠 Conversation Memory
- 📈 Analytics Dashboard

---

# 📷 Screenshots

### Home Page

<img src="<img width="1672" height="941" alt="App_Screenshot" src="https://github.com/user-attachments/assets/45d65919-7fd3-435b-80ed-50e9a9fd8173" />" width="100%">

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Developer

**Jagannath Sahoo**

GitHub: https://github.com/jagannathsahoo6370

---

<div align="center">

### ⭐ If you like this project, don't forget to Star the repository!

Made with ❤️ using Python, Streamlit, LangChain, Google Gemini & Groq

</div>
