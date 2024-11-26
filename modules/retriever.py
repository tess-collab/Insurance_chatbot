from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from config.settings import settings
from modules.file_handler import extract_text_from_pdf



def process_pdf(file_path: str):
    """
    Process the uploaded PDF and add its content to the vector store.
    """
    
    text = extract_text_from_pdf(file_path)

    # Split text into chunks for embedding
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_text(text)

    # Create embeddings and FAISS index
    embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
    faiss_index = FAISS.from_texts(texts=chunks, embedding=embeddings)

    # Save the FAISS index
    faiss_index.save_local(settings.EMBEDDINGS_PATH)

def get_retrieval_chain(llm):
    """
    Create a retrieval chain using the FAISS index.
    """
    embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
    faiss_index = FAISS.load_local(settings.EMBEDDINGS_PATH, embeddings, allow_dangerous_deserialization=True)

    retriever = faiss_index.as_retriever()
    retrieval_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return retrieval_chain
