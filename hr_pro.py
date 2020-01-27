print("Welcome to Hr Pro 2019")

def options():
        print("""1. Show Employees
    2. Show Managers
    3. Add An Employee
    4. Add A Manager
    5. Exit""")
    print()

options() 

class Employee:
    def __init__ (self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
    
    def get_working_years(self):
        today = 2020
        years =  today - int(self.employment_year)
        return years

    def __str__(self):
        return "name: %s, age: %d, salary: %d, working years: %d" % (self.name,int(self.age), int(self.salary),self.get_working_years)
    

class Manager (Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year):
        self.bonus_percentage = bonus_percentage
        
    def get_bonus(self):
        return float(self.bonus_percentage)* int(self.salary)

    def __str__(self):
       return "name: %s, age: %d, salary: %d, bonus %d" % (self.name,int(self.age), int(self.salary),self.bonus)


Employee[]
Manager[]

option = int(input("what would you like to do?"))

while option != 5:
    if option == 1:
        for employee in employees:
            print(employee)
        option = int(input("What would you like to do?"))
    elif option == 2:
        for manager in managers:
            print("managers")
        option =  int(input("What would you like to do?"))
    elif option == 3:
        name= input("Name: ")
        age = int(input("Age:"))
        salary= int(input(Salary:))
        employement =int(input("Employment year: "))
        employee = Employee(name, age, salary, employment)
        employee.append(employee)
        option = int(input("Wha would you like to do? "))
    elif option == 4:
        name= input("Name: ")
        age = int(input("Age:"))
        salary= int(input(Salary:))
        employement =int(input("Employment year: "))
        manager = Manager(name, age, salary, employment, bonus)
        employee.append(employee)
        option = int(input("Wha would you like to do? "))



# user_input = int("what would you like to do?")
#     while user_input = 5:
#         if user_input == 1:
#             for employee in Employee
#             print(Employee)
#         user_input = int(print("What would you like to do?"))
#             elif user_input == 2:
#             for manager in Manager
#             print(Manager)
#         user_input = int(print("What would you like to do?"))
#         if user_input = 3:
#             for 



