students = ("sunitha", "RAVI", "aNu")

formatted = tuple(name.capitalize() for name in students)

print(formatted)

subjects = ("Math", "Science", "English", "Math", "Science")

total_subjects = len(subjects)
unique_subjects = tuple(set(subjects))

print("Total Subjects:", total_subjects)
print("Unique Subjects:", unique_subjects)

feedback = (" good course ", " excellent ", "average ")

cleaned = tuple(f.strip() for f in feedback)

print(cleaned)

names = ("Anu", "Ravi", "John")
courses = ("Python", "SQL", "Power BI")

combined = tuple(names[i] + "-" + courses[i] for i in range(len(names)))

print(combined)

emails = ("anu@gmail.com", "ravi@yahoo.com", "john@edu.com")

domains = tuple(email.split("@")[1] for email in emails)

print(domains)