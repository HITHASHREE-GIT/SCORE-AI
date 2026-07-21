from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from security.pii_redactor import pii_redactor
import time

class SecurityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log request
        start_time = time.time()
        
        # Check for PII in request
        if request.method == "POST" and "/v1/chat" in request.url.path:
            body = await request.body()
            # Redact PII from request body (simplified)
            # In production, parse JSON and redact specific fields
        
        response = await call_next(request)
        
        # Add security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        
        return response