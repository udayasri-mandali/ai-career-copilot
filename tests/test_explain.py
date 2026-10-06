from app.llm import explain_match

requirement = "Strong Python programming skills"

evidence = """
Programming: Data Structures and Algorithms, Python (OOPS), C++ (Basics), Java (Basics)
Built a Linear Regression model using Python and Scikit-learn to predict semester GPA
"""

result = explain_match(
    requirement,
    evidence,
)

print("\nFINAL ANALYSIS:")
print(result)