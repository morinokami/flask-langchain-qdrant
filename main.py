from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)

app = FastAPI()

class ChatPayload(BaseModel):
    message: str

@app.post("/chat")
async def chat(payload: ChatPayload):
    llm = ChatOpenAI(temperature=0.2)
    messages = [
        SystemMessage(content="Tell me something funny."),
        HumanMessage(content=payload.message)
    ]
    response = llm(messages)
    return {
        "message": payload.message,
        "answer": response.content,
    }
