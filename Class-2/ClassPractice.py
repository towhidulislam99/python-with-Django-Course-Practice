in1 = input("Please Enter Your Name Here: ")
intocon = in1.upper()
print("The Name Format is Capital Word: "+intocon)

intocon1 = in1.lower()
print("The Name Format is Lower Word: "+intocon1)

intocon2 = in1.capitalize()
print("The Name Format is Capitalized Word: "+intocon2)


value = "mti"
value1 = value.replace('mti' ,'Md. Towhidul Islam')
print(value1)

val = "led colorful fiber christmas tree shaped lamp night light for e desk deco"
val1 = val.replace('fiber christmas', 'metal colorless')
print(val1)

cnt = val.count('c')
print(cnt)

pref = val.startswith('led')
print(pref)
pref1 = val.endswith('desk')
print(pref1)
