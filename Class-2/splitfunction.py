demo = "Bagdha is my village"
slp = demo.split(" ")
print(slp)

dom = slp[0] + slp[1]
print(dom)


in1 = input("Please Enter Your Name Here: ")
in2 = input("Please Enter Your Email Here: ")

insp1 = in1.split()
insp2 = in2.split()

if len(insp1) == 0 or len(insp2) == 0:
    print("Data Cannot be Inserted")
else:
    print("Data Successfully Inserted")

inp1 = input("Please Enter the first and last name here: ")
inpsp = inp1.split()

if len(inpsp) < 2:
    print("Please Enter the Last Name here, Data Cannot be Stored")
else:
    print("Data Successfully Stored Here")
