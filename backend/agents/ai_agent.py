from openai import OpenAI

from sqlalchemy.orm import Session

from backend.config.settings import settings
from backend.services.memory_service import (
    save_memory,
    get_memory
)


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_ai_response(
    message: str,
    user_id: int = None,
    db: Session = None
):

    try:

        memory_context = ""

        if user_id and db:

            user_memory = get_memory(
                db,
                user_id,
                "user_info"
            )

            if user_memory:

                memory_context = (
                    "\nRemembered information: "
                    + user_memory.memory_value
                )


        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content":
                    "You are SCORE AI Assistant."
                    + memory_context
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )


        ai_response = (
            response
            .choices[0]
            .message
            .content
        )


        if user_id and db:

            if "my name is" in message.lower():

                name = (
                    message.lower()
                    .replace("my name is", "")
                    .strip()
                )

                save_memory(
                    db,
                    user_id,
                    "user_info",
                    "User name is " + name
                )


        return ai_response


    except Exception as e:

        return (
            "SCORE AI development mode. Error: "
            + str(e)
        )