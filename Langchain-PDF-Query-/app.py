import streamlit as st
from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os


def main():
    st.title("Give Power to Your PDFs")

    with st.sidebar:
        st.header("Configuration")
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        st.warning("Please enter your OpenAI API key.")
        return

    if uploaded_file:
        pdfreader = PdfReader(uploaded_file)
        raw_text = ""
        for i, page in enumerate(pdfreader.pages):
            content = page.extract_text()
            if content:
                raw_text += content

        st.write("PDF content extracted. Ready for queries.")

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=800,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_text(raw_text)

        embeddings = OpenAIEmbeddings()
        document_search = FAISS.from_texts(texts, embeddings)
        chain = load_qa_chain(OpenAI(), chain_type="stuff")

        query = st.text_input("Enter your query:")

        if query:
            docs = document_search.similarity_search(query)
            answer = chain.run(input_documents=docs, question=query)
            st.write("Answer:", answer)


if __name__ == "__main__":
    main()
