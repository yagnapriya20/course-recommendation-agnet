from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_explanation(profile, courses):

    prompt = f"""
You are an expert career advisor.

Student Background:
{profile['background']}

Current Skills:
{profile['skills']}

Career Goal:
{profile['goal']}

Recommended Courses:
{courses}

Explain:
1. Why these courses were selected.
2. Why this order is important.
3. How this path helps achieve the career goal.
"""

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content