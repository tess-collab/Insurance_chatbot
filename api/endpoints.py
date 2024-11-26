from fastapi import APIRouter, HTTPException
from modules.chatbot import ChatBot
from pydantic import BaseModel

# Initialize router
router = APIRouter()

# Initialize ChatBot instance
chatbot = ChatBot()

# Define request/response models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    result: str

@router.post("/chat/", response_model=QueryResponse)
async def chat(query: QueryRequest):
    """
    Interact with the chatbot by providing a query.
    """
    try:
        response = chatbot.get_response(query.query)  # Ensure get_response is implemented in ChatBot
        return QueryResponse(result=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
