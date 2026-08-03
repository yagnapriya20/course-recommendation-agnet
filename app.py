from recommender import recommend
from llm import generate_explanation

print("===== Course Recommendation Agent =====")

name = input("Enter your name: ")

background = input("Enter your educational background: ")

skills = input("Enter your current skills (comma separated): ")

goal = input("Enter your career goal: ")


student_profile = {
    "name": name,
    "background": background,
    "skills": [skill.strip() for skill in skills.split(",")],
    "goal": goal
}


recommendations = recommend(student_profile)


print("\n===== Personalized Learning Path =====")

for index, course in enumerate(recommendations, 1):

    print(f"\n{index}. {course['course']}")
    print("Reason:", course["reason"])

try:
    ai_explanation = generate_explanation(
        student_profile,
        recommendations
    )

except Exception:
    ai_explanation = """
Based on your background and career goal, this learning path
starts with foundational skills, builds practical knowledge,
and gradually moves towards advanced concepts required for your career.
"""


print("\n===== AI Career Advice =====")
print(ai_explanation)