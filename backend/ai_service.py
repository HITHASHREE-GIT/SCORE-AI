import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# If .env doesn't work, hardcode it (temporary fix)
# GEMINI_API_KEY = "AIzaSyAb8RN6IjdqY8vnL3lwLQZOBehF-gvp-inUqqEEmoiBVF7JkGHw"

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file!")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

def get_ai_response(prompt: str) -> str:
    """Get a simple response from Gemini AI"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def chat_with_ai(message: str, history: list = None) -> str:
    """Chat with AI with conversation history"""
    try:
        if history:
            chat = model.start_chat(history=history)
            response = chat.send_message(message)
            return response.text
        else:
            response = model.generate_content(message)
            return response.text
    except Exception as e:
        return f"Error: {str(e)}"