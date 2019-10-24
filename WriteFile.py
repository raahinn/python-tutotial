

student_file = open("student.txt", "a")

# print(student_file.readlines()[1])
student_file.write("\nID: 203300000345 \nName: dfafaTobi")

# creating new file
teacher_file = open("teacher.txt", "w")
teacher_file.write("teacher list- \n Mohammad 123md \n shohel 234sho")



student_file.close()