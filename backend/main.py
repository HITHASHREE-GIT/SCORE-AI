from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from api import auth, conversations, messages, routes, users, ai
from api import documents
from api import self_correction
from security.middleware import SecurityMiddleware
from security.rate_limit import limiter, setup_rate_limiting
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

app = FastAPI(title="SCORE AI API", version="2.0.0")

# Setup rate limiting
setup_rate_limiting(app)

# CORS Configuration - Add your production URLs here
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", 
        "http://localhost:5174", 
        "http://127.0.0.1:5173", 
        "http://localhost:8501",
        # Add your production URLs below
        # "https://your-frontend.vercel.app",
        # "https://score-ai-backend.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security Middleware
app.add_middleware(SecurityMiddleware)

# Include routers
app.include_router(auth.router)
app.include_router(conversations.router)
app.include_router(messages.router)
app.include_router(routes.router)
app.include_router(users.router)
app.include_router(ai.router)
app.include_router(documents.router)
app.include_router(self_correction.router)

@app.get("/")
def home():
    return {"message": "Welcome to SCORE AI API", "version": "2.0.0"}

@app.get("/health")
def health_check():
    return {"status": "SCORE AI is running", "version": "2.0.0"}

@app.get("/status")
def status():
    return {
        "project": "SCORE AI",
        "backend": "FastAPI",
        "version": "2.0.0",
        "database": "Connected",
        "vector_db": "ChromaDB",
        "ai": "Cohere Connected",
        "cache": "Redis (Optional)",
        "security": "Rate Limiting & Security Headers Enabled"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)