students = {}
n = int(input("Enter the number of students: "))

for i in range(n):
    print(f"\n--- Entering details for Student {i+1} ---")
    
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    reg_no = input("Enter register number: ").strip()
    dept = input("Enter department: ").strip()
    semester = int(input("Enter semester: "))
    total_mark = float(input("Enter total mark (out of 100): "))
    
    
    student = {
        'name': name,
        'roll_number': roll_no,
        'register_number': reg_no,
        'department': dept,
        'semester': semester,
        'total_mark': total_mark
    }
    
    
    if total_mark >= 90:
        grade = 'A'
    elif total_mark >= 82:
        grade = 'B'
    elif total_mark >= 75:
        grade = 'C'
    elif total_mark >= 60:
        grade = 'D'
    elif total_mark >= 50:
        grade = 'P'
    else:
        grade = 'F'  
    
    
    student['grade'] = grade
    students[name] = student

print("\n" + "="*60)
print("STUDENTS DETAILS BEFORE SORTING")
print("="*60)
for name, details in students.items():
    print(f"Name: {details['name']}")
    print(f"Roll No: {details['roll_number']}")
    print(f"Register No: {details['register_number']}")
    print(f"Department: {details['department']}")
    print(f"Semester: {details['semester']}")
    print(f"Total Mark: {details['total_mark']}")
    print(f"Grade: {details['grade']}")
    print("-" * 40)


sorted_students = dict(sorted(students.items(), key=lambda x: x[0], reverse=True))

print("\n" + "="*60)
print("STUDENTS DETAILS AFTER SORTING (Descending order by Name)")
print("="*60)
for name, details in sorted_students.items():
    print(f"Name: {details['name']}")
    print(f"Roll No: {details['roll_number']}")
    print(f"Register No: {details['register_number']}")
    print(f"Department: {details['department']}")
    print(f"Semester: {details['semester']}")
    print(f"Total Mark: {details['total_mark']:.2f}")
    print(f"Grade: {details['grade']}")
    print("-" * 40)
