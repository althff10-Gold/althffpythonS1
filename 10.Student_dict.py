student = {
    "name": "Althaf",
    "roll_number": 42,
    "register_number": "19799",
    "department": "Computer Applications",
    "semester": 1
}

student["total_mark"] = int(input("Enter the total Marks :"))

def grade(total_mark):
    if total_mark >= 90:
        return 'A'
    elif total_mark >= 85:
        return 'B'
    elif total_mark >= 80:
        return 'C'
    elif total_mark >= 75:
        return 'D'
    elif total_mark >= 60:
        return 'P'
    else:
        return 'F'
    
student["grade"] = grade(student["total_mark"])

del student["roll_number"]

print(student)

