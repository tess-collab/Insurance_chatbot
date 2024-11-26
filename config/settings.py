import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    # Paths and API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMBEDDINGS_PATH = "./data/embeddings/faiss_index.bin"
    UPLOADS_PATH = "./data/uploads/"

    def __init__(self):
        # Validate OPENAI_API_KEY
        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is missing from the environment variables. Please set it in your .env file.")

        # Validate UPLOADS_PATH
        if not os.path.isdir(self.UPLOADS_PATH):
            raise ValueError(f"UPLOADS_PATH is not a valid directory: {self.UPLOADS_PATH}")
        if not os.access(self.UPLOADS_PATH, os.R_OK):
            raise PermissionError(f"No read access to directory: {self.UPLOADS_PATH}")

        # Validate EMBEDDINGS_PATH directory
        embeddings_dir = os.path.dirname(self.EMBEDDINGS_PATH)
        if not os.path.exists(embeddings_dir):
            os.makedirs(embeddings_dir, exist_ok=True)  # Create embeddings directory if it doesn't exist

        print("Settings initialized successfully!")

    def list_pdf_files(self):
        """
        List all PDF files in the UPLOADS_PATH directory.
        """
        return [
            os.path.join(self.UPLOADS_PATH, f)
            for f in os.listdir(self.UPLOADS_PATH)
            if f.endswith(".pdf")
        ]


# Instantiate the settings object to validate on import
settings = Settings()
