class Employee:
    company = 'Indian National Service'

    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display_details(self):
        print('Employee Name : ', self.name)
        print('Employee Age : ', self.age)
        print('Employee Department : ', self.department)
        print('Employee Salary : ', self.salary)


john = Employee('John Doe', 26, 'Peon', 31000)

print(john.name)
print(john.age)
print(john.department)
print(john.salary)

print('*************************************')

john.display_details()


# Output:
# John Doe
# 26
# Peon
# 31000
# *************************************
# Employee Name :  John Doe
# Employee Age :  26
# Employee Department :  Peon
# Employee Salary :  31000