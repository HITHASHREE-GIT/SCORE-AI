import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in .env file!")

# Initialize Groq client
client = Groq(
    api_key=GROQ_API_KEY
)

# Groq model for SCORE AI
# Fast + suitable for demos
MODEL = "llama-3.1-8b-instant"


def get_ai_response(prompt: str) -> str:
    """
    Generate AI response from Groq
    Used by AI agents
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are SCORE AI, an intelligent cloud security "
                        "assistant. Provide clear, accurate and helpful responses."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1024
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Error: {str(e)}"



def chat_with_ai(message: str, history: list = None) -> str:
    """
    Chat function with conversation history support
    Used for chatbot conversations
    """

    try:

        messages = [
            {
                "role": "system",
                "content": (
                    "You are SCORE AI assistant. "
                    "Help users with cloud security monitoring, "
                    "threat detection and analysis."
                )
            }
        ]


        # Add previous conversation
        if history:
            messages.extend(history)


        # Add current user message
        messages.append(
            {
                "role": "user",
                "content": message
            }
        )


        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )


        return response.choices[0].message.content


    except Exception as e:
        return f"AI Error: {str(e)}"