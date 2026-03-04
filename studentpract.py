import json

with open("students.json") as file:
    students = json.load(file)

students["year"] = "3rd"

with open("students.json",'w') as file:
    json.dump(students, file, indent=2)