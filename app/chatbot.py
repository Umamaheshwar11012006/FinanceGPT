from app.prompts import SYSTEM_PROMPT


def generate_response(pipe, user_message):

    prompt = f"""
{SYSTEM_PROMPT}

User:
{user_message}

Assistant:
"""

    result = pipe(
        prompt,
        max_new_tokens=50,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"]