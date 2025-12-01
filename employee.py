class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary  
    
    
    def update_salary(self, new_salary):
        if new_salary >= 0:
            self.salary = new_salary
            print(f"Salary of {self.name} updated to {self.salary}")
        else:
            print("Error: Salary cannot be negative!")
    
    
    def display_details(self):
        print("="*50)
        print("EMPLOYEE DETAILS")
        print("="*50)
        print(f"Name        : {self.name}")
        print(f"Designation : {self.designation}")
        print(f"Monthly Salary : {self.salary:,.2f}")
        print(f"Annual Income  : {self.calculate_annual_income():,.2f}")
        print("="*50)
    
    
    def calculate_annual_income(self):
        return self.salary * 12



print("Creating Employee Records...\n")

emp1 = Employee("Amit Sharma", "Software Engineer", 75000)
emp2 = Employee("Priya Singh", "Senior Manager", 120000)
emp3 = Employee("Rahul Verma", "Data Analyst", 60000)


print("INITIAL EMPLOYEE DETAILS")
emp1.display_details()
emp2.display_details()
emp3.display_details()


print("\nUPDATING SALARIES...\n")
emp1.update_salary(85000)
emp1.update_salary(130000)
emp3.update_salary(65000)        

print("\nUPDATED EMPLOYEE DETAILS")
emp1.display_details()
emp2.display_details()
emp3.display_details()
