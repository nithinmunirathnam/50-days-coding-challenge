students = ("Anu", "Ravikumar", "Jo")

longest_name = max(students, key=len)
print("Longest Name:", longest_name)

subjects = ("Math", "Science", "English")

result = ", ".join(subjects)
print("Subjects:", result)

students = ("Anu", "Ravi")

reversed_names = tuple(name[::-1] for name in students)
print("Reversed Names:", reversed_names)

students = ("Anu", "Ravi")

vowels = "aeiouAEIOU"

for name in students:
    count = sum(1 for char in name if char in vowels)
    print(f"{name} → Vowels: {count}")

    courses = ("python", "sql", "power bi")

    result = ", ".join(course.upper() for course in courses)
    print("Courses:", result)