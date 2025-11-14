def read_number():
    while True:
        num_str = input("Enter a number with at least 4 digits: ")
        if num_str.isdigit() and len(num_str) >= 4:
            return int(num_str)
        else:
            print("Invalid input. Please enter a number with at least 4 digits.")

def reverse_number(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev


number = read_number()
reversed_number = reverse_number(number)
print(f"Original number: {number}")
print(f"Reversed number: {reversed_number}")
