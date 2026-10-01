import requests
import matplotlib.pyplot as plt

API_URL = "https://api.slingacademy.com/v1/sample-data/files/student-scores.json"


def fetch_student_data():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    if isinstance(data, dict) and "data" in data:
        return data["data"]

    return data


def calculate_scores(students):
    results = []

    for student in students:
        score_fields = [
            key for key in student
            if key.endswith("_score")
            and isinstance(student[key], (int, float))
        ]

        if not score_fields:
            continue

        average = sum(student[key] for key in score_fields) / len(score_fields)

        name = f'{student.get("first_name", "")} {student.get("last_name", "")}'.strip()

        results.append((name, average))

    return results


students = fetch_student_data()

results = calculate_scores(students)

overall_average = sum(score for _, score in results) / len(results)

print("Number of students:", len(results))
print("Overall average:", round(overall_average, 2))

for name, average in results[:10]:
    print(name, ":", round(average, 2))


names = [name for name, score in results[:20]]
averages = [score for name, score in results[:20]]

plt.figure(figsize=(12, 6))
plt.bar(names, averages)

plt.xlabel("Student")
plt.ylabel("Average Score")
plt.title("Average Student Scores")

plt.xticks(rotation=60)
plt.tight_layout()

plt.savefig("student_average_scores.png")

plt.show()