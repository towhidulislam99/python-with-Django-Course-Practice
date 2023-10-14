# class Employee:
#     def __init__(self,first,last,pay) :
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@gmail.com'
        
# emp1 = Employee('Towhidul','Islam','50000')
# emp2 = Employee('Nijamul','Islam','45000')

# print('{} {}.{}' .format(emp1.first, emp1.last, emp1.email))

# class employee:
#     def __init__(self,name):
#         self.name = name
#         print(self.name + "Created")

# emp1 = employee('Ayman')
# emp2= employee('Munjerin Sahid')
       
class Employee:
    
    # parametarize Constructor
    def __init__(self, name, no):
        self.name = name
        self.no = no
    # Instance Method
    def display(self):
        print(self.name, self.no)

# Create instances of the Employee class
emp1 = Employee("Ayman", 10000)
emp2 = Employee("Munjerin Sahid", 20000)

# Call the display method for the Employee instances
emp1.display()
emp2.display()