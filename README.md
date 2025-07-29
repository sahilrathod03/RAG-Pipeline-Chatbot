# 📄 Give Power to Your PDFs

A powerful Streamlit app that transforms how you interact with PDF documents using state-of-the-art language models.

## 🚀 Features

- **📤 PDF Upload**: Drag-and-drop interface to upload PDF files.
- **📄 Text Extraction**: Extracts clean text from each page using `PyPDF2`.
- **✂️ Text Chunking**: Automatically splits text into manageable chunks.
- **🧠 Interactive Q&A**: Ask natural language questions and get answers directly from your PDF.
- **🤖 OpenAI Integration**: Uses OpenAI LLMs for accurate and context-aware responses.
- **🔎 Vector Search**: Powered by FAISS and LangChain for semantic document retrieval.

---

## 🧠 Use Case

Whether you're working with:
- Research papers 📚
- Legal documents ⚖️
- Technical manuals 🔧

This app helps you **quickly search**, **ask questions**, or **summarize** content without reading every page.

### 💡 Example Queries
> “What are the key findings in the research paper?”  
> “Summarize the introduction section.”  
> “What challenges are mentioned in the AI field?”

---

## 🖥️ App Interface

![App Screenshot]("C:\Users\Programmer ChOicE\Langchain-PDF-Query-\image.png"](https://github.com/sahilrathod03/RAG-Pipeline-Chatbot/blob/main/Langchain-PDF-Query-/image.png)) <!-- Replace with actual image link -->

---

## 📦 Requirements

- Python 3.8+
- Streamlit
- PyPDF2
- LangChain
- FAISS
- OpenAI API Key

---

## 🔧 Installation

Clone the repository:
```bash
git clone https://github.com/amishkr22/Langchain-PDF-Query-.git
cd give-power-to-your-pdfs

pip install -r requirements.txt

export OPENAI_API_KEY=your_key_here  # or enter in the app sidebar

