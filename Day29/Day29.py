students = {
    "Asha": {"Math": 78, "Science": 85, "English": 67},
    "Ravi": {"Math": 35, "Science": 40, "English": 50},
    "John": {"Math": 90, "Science": 92, "English": 88}
}

totals = {}
averages = {}
failed_students = []

# 1. Calculate total & average
for student, marks in students.items():
    total = sum(marks.values())
    average = total / len(marks)

    totals[student] = total
    averages[student] = average

    print(f"{student} -> Total: {total}, Average: {average:.2f}")

    # 3. Check for failed students
    for subject, mark in marks.items():
        if mark < 40:
            failed_students.append(student)
            break  # No need to check further subjects

# 2. Identify top scorer
top_scorer = max(totals, key=totals.get)

print("\nTop Scorer:", top_scorer, "with", totals[top_scorer], "marks")

# 3. Failed students
print("Failed Students:", failed_students)