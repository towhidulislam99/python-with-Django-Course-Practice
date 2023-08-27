nameFirst = input("Please Enter the First Name: ")
nameSecond = input("Please Enter the Last Name: ")
email = input("Please Enter Your Email Here: ")
dateofBirth = input("Enter Date Of Birth: ")
gender = input("Enter Gender Here: ")

if len(nameFirst) == 0 or len(nameSecond)== 0 or len(email) == 0 or len(dateofBirth) == 0 or len(gender) == 0:
    print("Please Fill the all Information in this form you can'n fill out full form your information cannot show")

else:
     print("Name: "+nameFirst, nameSecond) 
     print("E-Mail: "+email)
     print("Date Of Birth: "+dateofBirth)
     print("Gender: "+gender)

