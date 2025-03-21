#Simple inheritance
#1.Base class
#2.Derived class (from line 11)
'''class Person:
    def __init__(self):
        self.fname = input("Enter the first name: ")
        self.lname = input("Enter the last name: ")
    def show(self):
        print("firstname: ", self.fname)
        print("lastname: ", self.lname)
class Employee(Person):
    def __init__(self):
        Person.__init__(self)
        self.salary = input("Enter the salary: ")
    def show(self):
        Person.show(self)
        print("Salary = ", self.salary) 
        
obj = Employee()
obj.show()   '''

#Multilevel inheritance

class Person:
    def __init__(self):
        self.fname = input("Enter the first name: ")
        self.lname = input("Enter the last name: ")

    def show_person(self):
        print("First Name: ", self.fname)
        print("Last Name: ", self.lname)

class Employee(Person):
    def __init__(self):
        Person.__init__(self)
        self.employee_id = input("Enter the employee ID: ")
        self.department = input("Enter the department: ")

    def show_employee(self):
        self.show_person()
        print("Employee ID: ", self.employee_id)
        print("Department: ", self.department)

class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.salary = input("Enter the salary: ")

    def show_manager(self):
        self.show_employee()
        print("Salary: ", self.salary)
        

obj = Manager()
obj.show_manager()



#Multiple Inheritance
'''
class person:
    def __init__(self):
        self.fname = input("Enter the first name: ")
        self.lname = input("Enter the last name: ")

    def show_person(self):
        print("First Name: ", self.fname)
        print("Last Name: ", self.lname)

class department:
    def __init__(self):
        self.deptname = input("Enter the dept name: ")
        self.deptId = input("Enter the dept Id: ")
    
    def show_department(self):
        print("Dept Name: ", self.deptname)
        print("Dept Id: ", self.deptId)
        
class student(person,department):
    def __init__(self):
        #super().__init__()
        person.__init__(self)
        department.__init__(self)
        self.sId = input("Enter the student ID: ")
    def show(self):
        person.show_person(self)
        department.show_department(self)
        print("Student Id: ", self.sId)

s1= student()
s1.show()'''

#Hybrid inheritance

        