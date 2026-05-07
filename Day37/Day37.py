def get_marks():
    marks = []

    for i in range(1, 4):
        mark = int(input(f"Enter marks for Subject {i}: "))
        marks.append(mark)

    return marks

def calculate_total(marks):
    return sum(marks)

def calculate_average(total):
    return total / 3
def get_grade(avg):

    if avg >= 90:
        return "A"

    elif avg >= 75:
        return "B"

    elif avg >= 50:
        return "C"

    else:
        return "D"

marks = get_marks()

total = calculate_total(marks)

average = calculate_average(total)

grade = get_grade(average)

print("\n----- Student Report -----")
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)