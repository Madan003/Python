students = {
    1 :{
        "name": "madan",
        "age": 20,
        "grade": "BE in CSE"
    },
    2 :{
        "name": "kiran",
        "age": 21,
        "grade": "BE in ISE"
    },
    3: {
        "name": "jeevan",
        "age": 22,
        "grade": "BE in ECE"
    }
}

print(students.items())

print(students.get(3,{}).get("name","not found"))

students[1]["grade"] = "M tech"

#deleting
students.pop(3)

print(students)

#updating
students[2]["name"] = "gagan"

print(students)