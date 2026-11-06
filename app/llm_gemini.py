import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)
def LLmGemini(prompt):
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )
    return response.text or ""
def explain_match(requirement, evidence):

    prompt = f"""
You are a resume-job matching assistant.

Use ONLY the resume evidence provided below.

Job requirement:
{requirement}

Resume evidence:
{evidence}

Write a concise analysis with exactly two parts:

Match:
Explain what evidence from the resume supports the requirement.

Gap:
Mention only a genuine weakness that can be inferred from the requirement
and the provided evidence. If there is no clear weakness, say "No clear gap."

Do not invent skills, certifications, experience, or technologies.
Do not repeat the instruction.
Do not discuss information outside the evidence.
"""

    explanation = LLmGemini(prompt)

    if not explanation:
        return ""

    return explanation.strip()