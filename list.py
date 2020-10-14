student = ["student1","student2","student3"]

print(student)

print("=======================================")

student.append("student4")

print(student) #append method

print("================================")

student.insert(0,"student0")
print(student)

print("=================================")

student.pop();

print(student)

print("================================")

print(student[0])

print("===============================")

student[1] = "student0.1"
print(student)

print("=================================")


print(student[1:4])

print("===================================")

print(student[-4:-1])

print("========================")

print(student)

for demo in student:
    print(demo)

print("==============================")

student.clear()

print(student)

print("=================================")

student.append("AllClear")

print(student)
