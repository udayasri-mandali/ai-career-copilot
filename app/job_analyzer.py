import re
def extract_requirements(job_description):
    
    # Split the job description into lines or sentences.
    parts = re.split(
        r"\n+|(?<=[.!?])\s+",
        job_description,
    )

    requirements = []

    section_headings = {
        "requirements",
        "required skills",
        "qualifications",
        "preferred qualifications",
        "responsibilities",
        "what you'll do",
        "what you will do",
        "what we're looking for",
        "what we are looking for",
    }

    for part in parts:
        text = part.strip(" \t•-*")

        if not text:
            continue

        if text.lower().rstrip(":") in section_headings:
            continue

        # Ignore very short fragments, not specific skill names.
        if len(text.split()) >= 3:
            requirements.append(text)

    return requirements
