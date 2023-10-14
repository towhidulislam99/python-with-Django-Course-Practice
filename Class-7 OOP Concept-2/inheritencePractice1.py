class Employee:
    def __init__(self, id, name, address, salary):
        self.id = id
        self.name = name
        self.address = address
        self.salary = salary

class EmpDepartment:
    def __init__(self, depname, deplocation):
        self.depname = depname
        self.deplocation = deplocation

class EmployeeData(Employee, EmpDepartment):
    def __init__(self, id, name, address, salary, depname, deplocation):
        Employee.__init__(self, id, name, address, salary)
        EmpDepartment.__init__(self, depname, deplocation)

    def display(self):
        print(f"Employee Info: {self.id} {self.name} {self.address} {self.salary}")
        print(f"Department Info: {self.depname} {self.deplocation}")

emp = EmployeeData("10", "Towhidul Islam", "Bagdha", "10000", "Software Department", "202 No Room")
emp.display()