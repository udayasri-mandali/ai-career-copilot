from huggingface_hub import InferenceClient
def LLm(prompt):
    client = InferenceClient()
    response = client.chat.completions.create(
        model="Qwen/Qwen3-0.6B:featherless-ai",
        messages=[
            {
                "role": "user",
                "content": (
                    prompt
                ),
            }
        ],
        max_tokens=500,temperature=0.2,extra_body={"enable_thinking":False}
    )

    return response.choices[0].message.content or ""
    
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

    explanation = LLm(prompt)

    if not explanation:
        return ""

    return explanation.strip()