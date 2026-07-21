from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from services.simple_vector_service import vector_service
from security.rate_limit import limiter
from typing import List
import PyPDF2
import io

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/upload")
@limiter.limit("5/minute")
async def upload_document(request: Request, file: UploadFile = File(...)):
    try:
        content = await file.read()
        
        if file.filename.endswith('.pdf'):
            text = extract_pdf_text(content)
        elif file.filename.endswith('.txt'):
            text = content.decode('utf-8')
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        chunks = split_text(text)
        
        doc_ids = []
        for i, chunk in enumerate(chunks):
            doc_id = vector_service.add_document(
                text=chunk,
                metadata={"source": file.filename, "chunk": i}
            )
            doc_ids.append(doc_id)
        
        return {
            "message": "Document uploaded successfully",
            "document_id": doc_ids,
            "chunks": len(chunks),
            "filename": file.filename
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search")
@limiter.limit("20/minute")
def search_documents(request: Request, query: str, n_results: int = 5):
    results = vector_service.search(query, n_results)
    return {"results": results}

@router.get("/")
def get_all_documents():
    documents = vector_service.get_all_documents()
    return {"documents": documents}

def extract_pdf_text(content: bytes) -> str:
    try:
        pdf_file = io.BytesIO(content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading PDF: {str(e)}")

def split_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    if not text:
        return []
    
    words = text.split()
    if len(words) <= chunk_size:
        return [text]
    
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        if chunk:
            chunks.append(chunk)
    return chunks