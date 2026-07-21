from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from services.vector_service import vector_service
from security.rate_limit import limiter
from typing import List
import PyPDF2
import io

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/upload")
@limiter.limit("5/minute")
async def upload_document(request: Request, file: UploadFile = File(...)):
    # ... existing code
    pass

@router.get("/search")
@limiter.limit("20/minute")
def search_documents(request: Request, query: str, n_results: int = 5):
    # ... existing code
    pass