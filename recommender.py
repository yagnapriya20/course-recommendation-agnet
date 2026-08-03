import json


def load_courses():
    with open("database/course-catalog.json", "r") as file:
        courses = json.load(file)

    return courses


def recommend(profile):

    courses = load_courses()

    learning_path = []

    completed_courses = []

    for course in courses:

        prerequisites = course["prerequisite"]

        available = True

        for prerequisite in prerequisites:
            if prerequisite not in completed_courses:
                available = False

        if available:

            learning_path.append({
                "course": course["course"],
                "reason": f"This course helps you achieve your goal of {profile['goal']}."
            })

            completed_courses.append(course["course"])

    return learning_path