from app.llm import LLm

response = LLm(
    "Explain in one sentence why Python is useful for machine learning."
)

print("\nFINAL:")
print(response)