from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, List, Dict
from agents.orchestrator import Orchestrator
from security.rate_limit import limiter
import asyncio

router = APIRouter(prefix="/v1", tags=["chat"])
orchestrator = Orchestrator()

class ChatRequest(BaseModel):
    query: str
    user_id: str
    session_id: str
    context: Optional[Dict] = None

class ChatResponse(BaseModel):
    status: str
    answer: Optional[str] = None
    citations: Optional[List[Dict]] = None
    scores: Optional[Dict] = None
    metadata: Optional[Dict] = None
    conflict_summary: Optional[str] = None
    options: Optional[List[str]] = None

@router.post("/chat", response_model=ChatResponse)
@limiter.limit("10/minute")
async def chat(request: Request, chat_request: ChatRequest):
    try:
        print(f"📨 Received query: {chat_request.query}")
        
        # Process query with orchestrator
        result = await orchestrator.process_query(chat_request.query)
        
        print(f"📊 Result status: {result.get('status')}")
        
        if result['status'] == 'SUCCESS':
            return ChatResponse(
                status="SUCCESS",
                answer=result.get('answer', 'No answer provided'),
                citations=result.get('citations', []),
                scores=result.get('scores', {}),
                metadata={
                    "attempts": result.get('attempts', 1),
                    "reformulated_query": result.get('reformulated_query')
                }
            )
        else:
            return ChatResponse(
                status="CONFLICT_DETECTED",
                conflict_summary=result.get('message', "Could not find sufficient information"),
                options=["Option A", "Option B", "Provide more context"]
            )
            
    except Exception as e:
        print(f"❌ Chat error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))