# # Variable Name Validation
# my_var = "Towhid"
# myvar = "Towhid"
# myVar = "Towhid"
# MYvar = "Towhid"
# MYVAR = "Towhid"

# #string Declare in python
# demo = '''
# Salman
# Md 
# Sultan
# '''
# print (demo)

# list = ['Bangla','English','Mathematics']
# print (list)
# print (len(list))
# list1 = list.append('physics')
# print(list)
# list2 = ['Apple','Orange','Mango']
# list3 = list2.remove('Apple')
# print(list3)

# for x in "banana":
#     print(x)
    
# name = 'i am human and i am honest'
# print(len(name))


# txt = 'i am human'
# if "am" in txt:
#     print("Am in Present Here")
    
# to = "for being a man"
# print(to[2:8])
# print(to[:2])
# print(to[2:])
# txt = "Bangladesh is our Motherland"
# change = txt.upper()
# print(change)
# change1 = txt.lower()
# print(change1)
# change3 = txt.capitalize()
# print(change3)
# txt = "Bangladesh is our Motherland"
# print(txt.strip())
# print(txt.replace("Bangladesh", "Bagdha"))
# print(txt.split())


# a = "hello world"
# b = "Mohasin Howlader"
# print( a + b)


# age = 28
# thout = "my Name is John and my Age is: {}"
# print(thout.format(age))

# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

# list = ["bangla","English","Math","physics"]
# for index, list in enumerate (list):
#    print(f"Index: {index}: {list} ") 
   
# list2 = ["Apple","Banana","Orange","Cherry"]
# for index, list2 in enumerate (list2,start=1):
#     print(f"Index: {index}: {list2}")

employee_id = [1,2,3,4,5]
employee_name = ["Mahidul","Sahidul","Mominul","Khalilul","Touiobur"]
employee_salary = [10000,40000,45000,30000,55000]
employee_info = zip(employee_id,employee_name,employee_salary)

for employee_id,employee_name,employee_salary in employee_info:
   print("Employee ID: ", employee_id, "Employee Name: ", employee_name, "Employee Salary: ",employee_salary)
    

