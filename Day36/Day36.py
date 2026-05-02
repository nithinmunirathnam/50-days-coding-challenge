data = [
    {"batch": "b7", "name": "Anil", "consumption": 72, "live": 65, "recording": 70, "assignment_sub": 80, "assignment_score": 75},
    {"batch": "b7", "name": "Meena", "consumption": 45, "live": 50, "recording": 55, "assignment_sub": 40, "assignment_score": 35},
    {"batch": "b7", "name": "Ravi", "consumption": 18, "live": 20, "recording": 25, "assignment_sub": 10, "assignment_score": 15},
    {"batch": "b7", "name": "Pooja", "consumption": 85, "live": 75, "recording": 80, "assignment_sub": 90, "assignment_score": 88},
    {"batch": "b7", "name": "Kiran", "consumption": 30, "live": 40, "recording": 45, "assignment_sub": 25, "assignment_score": 28},

    {"batch": "b8", "name": "Asha", "consumption": 90, "live": 85, "recording": 88, "assignment_sub": 92, "assignment_score": 90},
    {"batch": "b8", "name": "Manoj", "consumption": 55, "live": 60, "recording": 65, "assignment_sub": 50, "assignment_score": 45},
    {"batch": "b8", "name": "Deepa", "consumption": 22, "live": 30, "recording": 35, "assignment_sub": 20, "assignment_score": 18},
    {"batch": "b8", "name": "Rahul", "consumption": 78, "live": 70, "recording": 75, "assignment_sub": 80, "assignment_score": 76},
    {"batch": "b8", "name": "Sneha", "consumption": 10, "live": 15, "recording": 20, "assignment_sub": 5, "assignment_score": 8},

    {"batch": "b9", "name": "Vikram", "consumption": 88, "live": 82, "recording": 90, "assignment_sub": 85, "assignment_score": 80},
    {"batch": "b9", "name": "Divya", "consumption": 60, "live": 68, "recording": 72, "assignment_sub": 65, "assignment_score": 60},
    {"batch": "b9", "name": "Arjun", "consumption": 35, "live": 40, "recording": 50, "assignment_sub": 30, "assignment_score": 25},
    {"batch": "b9", "name": "Neha", "consumption": 95, "live": 90, "recording": 95, "assignment_sub": 98, "assignment_score": 96},
    {"batch": "b9", "name": "Karthik", "consumption": 15, "live": 20, "recording": 25, "assignment_sub": 10, "assignment_score": 12}
]


def calculate_average(values):
    return sum(values) / len(values)



def find_top_performers(data, column, threshold):
    top_students = []

    for student in data:
        if student[column] >= threshold:
            top_students.append(student["name"])

    return top_students



def find_at_risk_students(data, column, threshold):
    risk_students = []

    for student in data:
        if student[column] < threshold:
            risk_students.append(student["name"])

    return risk_students



def batch_summary(data):

    batches = {}

    for student in data:
        batch = student["batch"]

        if batch not in batches:
            batches[batch] = {
                "consumption": [],
                "live": [],
                "assignment_sub": []
            }

        batches[batch]["consumption"].append(student["consumption"])
        batches[batch]["live"].append(student["live"])
        batches[batch]["assignment_sub"].append(student["assignment_sub"])

    summary = {}

    for batch, values in batches.items():
        summary[batch] = {
            "total_students": len(values["consumption"]),
            "avg_consumption": round(calculate_average(values["consumption"]), 1),
            "avg_attendance": round(calculate_average(values["live"]), 1),
            "avg_assignment_submission": round(calculate_average(values["assignment_sub"]), 1)
        }

    return summary



def rank_batches(batch_data):

    best_batch = ""
    highest_score = 0

    for batch, details in batch_data.items():

        overall = (
            details["avg_consumption"] +
            details["avg_attendance"] +
            details["avg_assignment_submission"]
        ) / 3

        if overall > highest_score:
            highest_score = overall
            best_batch = batch

    return best_batch


summary = batch_summary(data)

print("Batch Summary")
for batch, details in summary.items():
    print(batch, "-", details)

print()

best = rank_batches(summary)
print("Best Batch:", best)

print()

top_students = find_top_performers(data, "consumption", 80)
print("Top Performers:", top_students)

print()

risk_students = find_at_risk_students(data, "consumption", 20)
print("At-Risk Students:", risk_students)