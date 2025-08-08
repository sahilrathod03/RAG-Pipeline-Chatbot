# 📄 Give Power to Your PDFs

A powerful **Streamlit** app that revolutionizes how you interact with PDF documents using **state-of-the-art language models** and **vector-based search**.

---

## 🚀 Features

- **📤 PDF Upload**: Simple drag-and-drop interface to upload PDF files.  
- **📄 Text Extraction**: Extracts clean text from each page using `PyPDF2`.  
- **✂️ Text Chunking**: Splits extracted text into smaller, meaningful chunks for efficient processing.  
- **🧠 Interactive Q&A**: Ask natural language questions and get context-aware answers directly from your PDF.  
- **🤖 OpenAI Integration**: Harnesses the power of OpenAI LLMs for accurate responses.  
- **🔎 Vector Search**: Uses **FAISS** and **LangChain** for semantic similarity-based document retrieval.  

---

## 🧠 Use Cases

Perfect for quickly searching, summarizing, or querying:

- Research Papers 📚  
- Legal Documents ⚖️  
- Technical Manuals 🔧  
- Business Reports 📊  
- Study Materials 📖  

---

### 💡 Example Queries

> “What are the key findings in the research paper?”  
> “Summarize the introduction section.”  
> “What challenges are mentioned in the AI field?”  

---

## 🖥️ App Interface

![App Screenshot](https://github.com/sahilrathod03/RAG-Pipeline-Chatbot/blob/main/Langchain-PDF-Query-/image.png)

---

## 📦 Requirements

- Python 3.8+  
- [Streamlit](https://streamlit.io/)  
- [PyPDF2](https://pypi.org/project/PyPDF2/)  
- [LangChain](https://www.langchain.com/)  
- [FAISS](https://faiss.ai/)  
- [OpenAI API Key](https://platform.openai.com/)  

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/sahilrathod03/RAG-Pipeline-Chatbot.git
cd RAG-Pipeline-Chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your **OpenAI API key** (replace `your_key_here` with your actual key):

```bash
export OPENAI_API_KEY=your_key_here   # For macOS/Linux
set OPENAI_API_KEY=your_key_here      # For Windows (Command Prompt)
$env:OPENAI_API_KEY="your_key_here"   # For PowerShell
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then, open the displayed **local URL** in your browser to start using the application.

---

## 📂 Project Structure

```
RAG-Pipeline-Chatbot/
│
├── Langchain-PDF-Query-/
│   ├── app.py               # Main Streamlit application
│   ├── requirements.txt     # Dependencies
│   ├── image.png            # Screenshot
│   └── ...other files
│
└── README.md
```

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **NLP**: OpenAI GPT models via LangChain  
- **Vector Database**: FAISS  
- **PDF Processing**: PyPDF2  

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork this repo, open issues, or submit pull requests.

---

## 📜 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute with attribution.
