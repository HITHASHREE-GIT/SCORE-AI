from google import genai

from backend.config.settings import settings


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def generate_ai_response(message: str):

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=message
        )

        return response.text


    except Exception:

        # Temporary fallback until Gemini quota is enabled
        return (
            "SCORE AI Assistant received your message: "
            + message
            + ". "
            "I am currently running in development mode."
        )