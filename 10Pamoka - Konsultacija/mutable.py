students = {}
grade1 = []
grade2 = []
students_num = int(input('Enter a number of students: '))
student1 = input('Enter a student name: ')
for stud_grade in range(3):
    grades1 = int(input(f'Enter grade for {student1} (0-100): '))
    if 0 <= grades1 <= 100:
        grade1.append(grades1)
    else:
        print('Please enter a valid grade between 0 and 100')
student2 = input('Enter a student name: ')
for stud_grade in range(3):
    grades2 = int(input(f'Enter grade for {student2} (0-100): '))
    if 0 <= grades2 <= 100:
        grade2.append(grades2)
    else:
        print('Please enter a valid grade between 0 and 100')

new_dict = {'name': student1, 'grade': grade1}
new_stud = {'name': student2, 'grade': grade2}
students.update(new_dict)
students.update(new_stud)

average1 = sum(grade1) / len(grade1)
print(f'Average grade for {student1}: {average1}')
average2 = sum(grade2) / len(grade2)
print(f'Average grade for {student2}: {average2}')

subjects = int(input('Enter a number of subjects: '))
if average1 > average2:
    print(f'Student {student1} has a higher averag`e grade')
elif average1 < average2:
    print(f'Student {student2} has a higher average grade')
else:
    print('Both students have the same average grade')