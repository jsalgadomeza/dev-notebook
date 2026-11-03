from fastapi import APIRouter
from pydantic import BaseModel
import httpx

router = APIRouter(
    prefix = "/llm",
    tags = ["llm"]
)

class LLMRequest(BaseModel):
    prompt: str

@router.post("/ask")
async def ask_llm(request: LLMRequest):
    async with httpx.AsyncClient(timeout=600) as client:
        response = await client.post(
            "http://localhost:11434/v1/chat/completions",
            json={
                "model": "llama3.2:3b",
                "messages": [{"role": "user", "content": request.prompt}],
            }
        )
    return {
        "answer": response.json()["choices"][0]["message"]["content"]
    }