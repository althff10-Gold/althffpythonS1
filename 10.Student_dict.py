student = {
    "name": "Nihal",
    "roll_number": 37,
    "register_number": "19857",
    "department": "Computer Applications",
    "semester": 1
}

student["total_mark"] = 85

def grade(total_mark):
    if total_mark >= 90:
        return 'A'
    elif total_mark >= 82:
        return 'B'
    elif total_mark >= 75:
        return 'C'
    elif total_mark >= 60:
        return 'D'
    elif total_mark >= 50:
        return 'P'
    else:
        return 'F'
    
student["grade"] = grade(student["total_mark"])

del student["roll_number"]

print(student)
