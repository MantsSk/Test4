
num_students = int(input("Enter the number of students: "))
num_of_subjects = 2

students = [] # idea that we will store here - [{"name": "Mantas", "grades": [40,60,100]}, {"name": "Laura", "grades": [50,70,90]}]

i = 0
for _ in range(num_students):
    name = input("Enter student name")

    grades = []
    for _ in range(num_of_subjects):
        grade = float(input(f"Enter grade for {name} (0-100"))
        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Please enter a valid grade between 0 and 100")

    student = {"name": name, "grades": grades} # {"name": "Mantas", "grades": [40,60,100]}
    students.append(student)

for student in students:
    average = sum(student['grades']) / len(student['grades'])
    print(f"Average grade for student {student['name']}: {average}")

def return_student_average(student):
    return sum(student['grades']) / len(student['grades'])

best_student = students[0]
for student in students:
    if return_student_average(student) > return_student_average(best_student):
        best_student = student

print(f"\nBest student: {best_student['name']} with an average grade of {sum(best_student['grades']) / len(best_student['grades']):.2f}")
