
student_file = open("student.txt", "r")

# print(student_file.readlines()[1])

for std in student_file.readlines():
    print(std)

student_file.close()

