from fastapi import FastAPI
from api.endpoints import router  # Import the router with your /chat endpoint

# Initialize FastAPI app
app = FastAPI(
    title="Insurance Chatbot API",
    description="An API for interacting with the insurance chatbot.",
    version="1.0.0"
)

# Include the router for chatbot interactions (defined in endpoints.py)
app.include_router(router)

# Optional: Add a root endpoint to verify the API is running
@app.get("/")
async def root():
    return {"message": "Welcome to the Insurance Chatbot API. Use /chat to interact with the bot."}






"""
from modules.chatbot import ChatBot
from config.settings import settings
import os

if __name__ == "__main__":
    bot = ChatBot()
    print("Welcome to the Insurance Chatbot!")

    print(os.path.abspath('./data/uploads/'))

    # Path to the folder containing uploaded PDFs
    folder_path = settings.UPLOADS_PATH

    # Ensure the folder path exists and is accessible
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        exit(1)

    print("Processing uploaded PDFs...")
    bot.process_uploaded_pdf(folder_path)

    # Start the chatbot
    bot.chat()
"""
    

