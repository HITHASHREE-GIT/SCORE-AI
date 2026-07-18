from fastapi import FastAPI

from backend.api import auth
from backend.api import users
from backend.api import routes
from backend.api import conversations
from backend.api import messages

from backend.database.connection import Base, engine

# Import models so tables are registered
from backend.models import user
from backend.models import conversation
from backend.models import message


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="SCORE AI",
    version="1.0.0"
)


# Routers

app.include_router(
    auth.router
)

app.include_router(
    users.router
)

app.include_router(
    routes.router
)

app.include_router(
    conversations.router
)

app.include_router(
    messages.router
)


@app.get("/")
def home():

    return {
        "message": "Welcome to SCORE AI API"
    }


@app.get("/health")
def health_check():

    return {
        "status": "SCORE AI is running"
    }


@app.get("/status")
def status():

    return {
        "project": "SCORE AI",
        "backend": "FastAPI",
        "database": "Connected"
    }