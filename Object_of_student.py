from Class_student import Student

student1 = Student("ehan", "cse", 3.00, False)
student2 = Student("dddffa", "cse", 4.00, False)
print(student1.on_probation)
print(student2.gpa)

print(f'{student1.name} honor: {student1.on_probation}')