employee_id = [1,2,3,4,5]
employee_name =["Towhid","Shourove","Ahad","Rahat","Rahman"]
emp_salary = [25000,30000,35000,40000,50000]

emp_info = zip(employee_id,employee_name,emp_salary)
print(list(emp_info))

employee_id = [1,2,3,4,5]
employee_name =["Towhid","Shourove","Ahad","Rahat","Rahman"]
employee_salary = [25000,30000,35000,40000,50000]
emp_info = zip(employee_id,employee_name,emp_salary)

for emp_id, emp_name, emp_salary in emp_info:
   print ("Employee_Id : ", emp_id, " Emploree_Name: ", emp_name, " Employee_salary: ", emp_salary)

# Python code to explain working of zip() function
# initializing lists
employee_id = [1,2,3,4,5]
employee_name =["Towhid","Shourove","Ahad","Rahat","Rahman"]
employee_salary = [25000,30000,35000,40000,50000]
# zip() to create zip object
emp_info = zip(employee_id,employee_name,employee_salary)

# Convert zipped bject as set
emp_info = set(emp_info)
print("The zipped Output: ", emp_info)

# Unzipped the values in different list
e_id, e_name, e_salary = zip(*emp_info)

# Print lists
print("Employee ID", e_id)
print("Employee Name: ", e_name)
print("Employee Salary", e_salary)



employee_id = [1,2,3,4,5,6,7]
employee_name =["Towhid","Shourove","Ahad","Rahat","Rahman"]
emp_salary = [25000,30000,35000,40000,50000,3000,]

emp_info = zip(employee_id,employee_name,emp_salary)
print(list(emp_info))  




