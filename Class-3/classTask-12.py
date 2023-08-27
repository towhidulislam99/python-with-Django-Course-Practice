print("Please provide your Marks for result:")
bangla = int(input("Bangla: "))
english = int(input("English: "))
mathematics = int(input("Mathematics: "))
socialscience = int(input("Social Science: "))
religion = int(input("Religion: "))
highermath = int(input("Higher Math: "))
physics = int(input("Physics: "))                         
chemistry = int(input("Chemistry: "))
biology = int(input("Biology: "))

print("\n")
print("***************Education Board Bangladesh*********************")
print("*******************Grade wise Result*********************")
#Bangla Subject Marks Calculate Grade Point  using if else condition
if bangla>=80 and bangla<=100 :
    point1 = 5.00
    print("Bangla: A+")
elif bangla>=70 and bangla<=79 :
    point1 = 4.00
    print("Bangla: A")
elif bangla>=60 and bangla<=69 :
    point1 = 3.50
    print("Bangla: A-")
elif bangla>=50 and bangla<=59 :
    point1 = 3.00
    print("Bangla: B")
elif bangla>=40 and bangla<=49 :
    point1 = 2.50
    print("Bangla: C")
elif bangla>=33 and bangla<40 :
    point1 = 2.00
    print("Bangla: D")
elif bangla>=1 and bangla<33 :
    point1 = 0.00
    print("Bangla: Fail")
else:
    print(" Please Input the Valid Mark Between 1 and 100 ")

# English Subject Marks Calculate Grade Point  using if else condition
if english>=80 and english<=100 :
    point2 = 5.00
    print("English: A+")
elif english>=70 and english<=79 :
    point2 = 4.00
    print("English: A")
elif english>=60 and english<=69 :
    point2 = 3.50
    print("English: A-")
elif english>=50 and english<=59 :
    point2 = 3.00
    print("English: B")
elif english>=40 and english<=49 :
    point2 = 2.50
    print("English: C")
elif english>=33 and english<40 :
    point2 = 2.00
    print("English: D")
elif english>=1 and english<33 :
    point2 = 0.00
    print("English: Fail")
else:
    print(" Please Input the Valid Mark Between 1 and 100 ")

# Mathematics Subject Marks Calculate Grade Point  using if else condition
if mathematics>=80 and mathematics<=100 :
    point3 = 5.00
    print("Mathematics: A+")
elif mathematics>=70 and mathematics<=79 :
    point3 = 4.00
    print("Mathematics: A")
elif mathematics>=60 and mathematics<=69 :
    point3 = 3.50
    print("Mathematics: A-")
elif mathematics>=50 and mathematics<=59 :
    point3 = 3.00
    print("Mathematics: B")
elif mathematics>=40 and mathematics<=49 :
    point3 = 2.50
    print("Mathematics: C")
elif mathematics>=33 and mathematics<40 :
    point3 = 2.00
    print("Mathematics: D")
elif mathematics>=1 and mathematics<33 :
    point3 = 0.00
    print("Mathematics: Fail")
else:
    print(" Please Input the Valid Mark Between 1 and 100 ")

# Social Science Subject Marks Calculate Grade Point  using if else condition
if socialscience>=80 and socialscience<=100 :
    point4 = 5.00
    print("Social Science: A+")
elif socialscience>=70 and socialscience<=79 :
    point4 = 4.00
    print("Social Science: A")
elif socialscience>=60 and socialscience<=69 :
    point4 = 3.50
    print("Social Science: A-")
elif socialscience>=50 and socialscience<=59 :
    point4 = 3.00
    print("Social Science: B")
elif socialscience>=40 and socialscience<=49 :
    point4 = 2.50
    print("Social Science: C")
elif socialscience>=33 and socialscience<40 :
    point4 = 2.00
    print("Social Science: D")
elif socialscience>=1 and socialscience<33 :
    point4 = 0.00
    print("Social Science: Fail")
else:
    print(" Please Input the Valid Mark Between 1 and 100 ")

# Religion Subject Marks Calculate Grade Point  using if else condition
if religion>=80 and religion<=100 :
    point5 = 5.00
    print("Religion: A+")
elif religion>=70 and religion<=79 :
    point5 = 4.00
    print("Religion: A")
elif religion>=60 and religion<=69 :
    point5 = 3.50
    print("Religion: A-")
elif religion>=50 and religion<=59 :
    point5 = 3.00
    print("Religion: B")
elif religion>=40 and religion<=49 :
    point5 = 2.50
    print("Religion: C")
elif religion>=33 and religion<40 :
    point5 = 2.00
    print("Religion: D")
elif religion>=1 and religion<33 :
    point5 = 0.00
    print("Religion: Fail")
else:
    print(" Please Input the Valid Mark Between 1 and 100 ")
              
# Higher Math Subject Marks Calculate Grade Point  using if else condition
if highermath>=80 and highermath<=100 :
    point6 = 5.00
    print("Higher Math: A+")
elif highermath>=70 and highermath<=79 :
    point6 = 4.00
    print("Higher Math: A")
elif highermath>=60 and highermath<=69 :
    point6 = 3.50
    print("Higher Math: A-")
elif highermath>=50 and highermath<=59 :
    point6 = 3.00
    print("Higher Math: B")
elif highermath>=40 and highermath<=49 :
    point6 = 2.50
    print("Higher Math: C")
elif highermath>=33 and highermath<40 :
    point6 = 2.00
    print("Higher Math: D")
elif highermath>=1 and highermath<33 :
    point6 = 0.00
    print("Higher Math: Fail")
else:
    print(" Please Input the Valid Mark Between 1 and 100 ")

# Physics Subject Marks Calculate Grade Point  using if else condition
if physics>=80 and physics<=100 :
    point7 = 5.00
    print("Physics: A+")
elif physics>=70 and physics<=79 :
    point7 = 4.00
    print("Physics: A")
elif physics>=60 and physics<=69 :
    point7 = 3.50
    print("Physics: A-")
elif physics>=50 and physics<=59 :
    point7 = 3.00
    print("Physics: B")
elif physics>=40 and physics<=49 :
    point7 = 2.50
    print("Physics: C")
elif physics>=33 and physics<40 :
    point7 = 2.00
    print("Physics: D")
elif physics>=1 and physics<33 :
    point7 = 0.00
    print("Physics: Fail")
else:
    print(" Please Input the Valid Mark Between 1 and 100 ")

# Chemistry Subject Marks Calculate Grade Point  using if else condition
if chemistry>=80 and chemistry<=100 :
    point8 = 5.00
    print("Chemistry: A+")
elif chemistry>=70 and chemistry<=79 :
    point8 = 4.00
    print("Chemistry: A")
elif chemistry>=60 and chemistry<=69 :
    point8 = 3.50
    print("Chemistry: A-")
elif chemistry>=50 and chemistry<=59 :
    point8 = 3.00
    print("Chemistry: B")
elif chemistry>=40 and chemistry<=49 :
    point8 = 2.50
    print("Chemistry: C")
elif chemistry>=33 and chemistry<40 :
    point8 = 2.00
    print("Chemistry: D")
elif chemistry>=1 and chemistry<33 :
    point8 = 0.00
    print("Chemistry: Fail")
else:
    print(" Please Input the Valid Mark Between 1 and 100 ")

# Biology Subject Marks Calculate Grade Point  using if else condition
if biology>=80 and biology<=100 :
    point9 = 5.00
    print("Biology: A+")
elif biology>=70 and biology<=79 :
    point9 = 4.00
    print("Biology: A")
elif biology>=60 and biology<=69 :
    point9 = 3.50
    print("Biology: A-")
elif biology>=50 and biology<=59 :
    point9 = 3.00
    print("Biology: B")
elif biology>=40 and biology<=49 :
    point9 = 2.50
    print("Biology: C")
elif biology>=33 and biology<40 :
    point9 = 2.00
    print("Biology: D")
elif biology>=1 and biology<33 :
    point9 = 0.00
    print("Biology: Fail")
else:
    print(" Please Input the Valid Mark Between 1 and 100 ")

#Checking whether the student has passed all the subjects in the Examination 
if (bangla <= 32 or english <= 32 or mathematics <= 32 or socialscience <= 32 or
    religion <= 32 or highermath <= 32 and physics <= 32 or chemistry <= 32 or biology <= 32):
    print("You are Fail in the Examination")
#if the Student Pass in the Examination all Subject then Calculate the Total Marks
else:
    total_marks = (bangla + english + mathematics + socialscience + religion +
                   highermath + physics + chemistry + biology)
    print("***********************Ministry of Education****************************")
    print("*********Intermediate and Secondary Education Boards Bangladesh*********")
    print("\n")
    print("*****SSC/Dakhil/Equivalent Result 2024*****")
    print("You obtain Total Mark in 9 Subject: " + str(total_marks))
# Grade calculate based on the total marks in the examination using if elif condition
if total_marks>=720 :
    print("Grade: A+")
elif total_marks>=630 :
    print("Grade: A")
elif total_marks>=540 :
    print("Grade: A-")
elif total_marks>=450 :
    print("Grade: B")
elif total_marks>=360 :
    print("Grade: C")
elif total_marks>=297 :
    print("Grade: D")
else:
    print("You are Fail in the Examination")

#total point calculate if the student passed all subject in the examination 
total_point = (point1 + point2 + point3 + point4 + point5 + point6 + point7 + point8 + point9)
#GPA calculate Avarage point
cgpa = total_point / 9
print("Your GPA: {:.2f}".format(cgpa))

#Calculate the percentage Based on the total marks 
percentage = (total_marks/900)*100
print("Your Percentage Marks is: {:.2f}%".format(percentage))
print("\n")

