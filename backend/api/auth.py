from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import hashlib
import jwt
import datetime

router = APIRouter(prefix="/auth", tags=["auth"])

SECRET_KEY = "your-secret-key-change-this"
ALGORITHM = "HS256"

class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

# Temporary in-memory database
users_db = {}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def create_token(email: str) -> str:
    payload = {
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/register")
def register(user: UserRegister):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    users_db[user.email] = {
        "name": user.name,
        "email": user.email,
        "password": hash_password(user.password)
    }
    
    token = create_token(user.email)
    return {
        "message": "User registered successfully",
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/login")
def login(user: UserLogin):
    if user.email not in users_db:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    stored_user = users_db[user.email]
    if stored_user["password"] != hash_password(user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token(user.email)
    return {
        "access_token": token,
        "token_type": "bearer"
    }