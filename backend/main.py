from fastapi import FastAPI

from backend.api import auth
from backend.api import users

from backend.database.connection import Base, engine


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="SCORE AI",
    version="1.0.0"
)


# Routers

app.include_router(auth.router)

app.include_router(users.router)



@app.get("/")
def home():

    return {
        "message": "Welcome to SCORE AI 🚀",
        "version": "1.0.0",
        "status": "Running"
    }



@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }