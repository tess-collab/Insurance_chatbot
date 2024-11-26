#from langchain.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from modules.retriever import get_retrieval_chain, process_pdf
from config.settings import settings
import os

class ChatBot:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0.7,
            model="gpt-3.5-turbo",
            openai_api_key=settings.OPENAI_API_KEY
        )

    def process_uploaded_pdf(self, folder_path: str):
        """
        Process all PDF files in the specified folder.
        """
        # List all PDF files in the folder
        pdf_files = [
            os.path.join(folder_path, file)
            for file in os.listdir(folder_path)
            if file.endswith(".pdf")
        ]

        if not pdf_files:
            print("No PDF files found in the directory.")
            return

        for pdf_file in pdf_files:
            print(f"Processing PDF: {pdf_file}")
            process_pdf(pdf_file)  # Process each PDF file
            print(f"Finished processing: {pdf_file}")

    def chat(self):
        """
        Start a chatbot session with RAG.
        """
        retrieval_chain = get_retrieval_chain(self.llm)
        print("Chatbot: Hello! Ask me anything about SBI Life insurance. (type 'exit' to quit)")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye!")
                break

            response = retrieval_chain.invoke({"query": user_input})
            print(f"Chatbot: {response['result']}")

    def get_response(self, query: str) -> str:
        """
        Handle user queries and return chatbot responses.
        """
        retrieval_chain = get_retrieval_chain(self.llm)
        response = retrieval_chain.invoke({"query": query})
        return response['result']
