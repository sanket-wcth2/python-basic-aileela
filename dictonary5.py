student = {"name": "Sanket","age": 20,"course": "Python",}
print(student)

print(student["name"])

student["grade"] = "B"
print(student) #add new pair

student["grade"] = "A"
print(student) #update value

print(student.keys()) #give all keys of student
print(student.values()) #give values

student.pop("grade")
print(student) #del

print(len(student)) #length

if "course" in student:
    print("Course is available") #check key exists

for key, value in student.items():
    print(key, ":", value)

#nested dict

students = {
    "student1": {
        "name": "Chaitany",
        "age": 19,
        "course": "C++"
    },
    "student2": {
        "name": "Aditya",
        "age": 21,
        "course": "Java"
    }
}
print(students)
