s = "i am Towhid"

print (type(s))

print (s)

print(s[-1])

print(len(s))

print (s[len(s)-1])

index = 0
x = "i am Programmer"
while index < len(x):
    print(x[index])
    index += 1

    for char in x:
        print(char)

    v = "hello python developer"
    s = v +" "+"With Django Framework"
    print (s);


d  = "development with Salman Vai"
e ="Python with Django"
print (d +" "+ e)

p = "Problem Solving"
print(p * 4 )


for x in range(0, 4):
    print("hi")

    d = "Development with Salman Bhai"
    u ="to be continue"
    i = "Salman Bhai"
    print(d[2:10])
    print(d[2:9:2])
    print(d in u)
    print(i in d)

    s1 = "I am Honest"
    s2 = "Honest"
    if s2 in s1:
        print("S1 is Found")
    else:
        print("Not Found")

       
g = "I Love the Movie '3 Idiots'"
h = 'i love This Movie "Dujone"'
print(g)
print(h)

k = g.count('o')
print(k)

l = g.find('s')
print(l)

w = "hello {}, I am {}.".format("Towhid","Towfiq")
print(w)
ew = "hello {0}, She is {1} .".format("Towhid", "Adhora")
print(ew)
tw = "Hello {speaker}, introduce {her}.".format(speaker="Towhid", her="Mehjabin")
print(tw)

Convert = "Binary: {0:b}, Octal: {0:o}, Hexadecimal: {0:x}".format(10)
print(Convert)