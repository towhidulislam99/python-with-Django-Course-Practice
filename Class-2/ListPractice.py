list = ["Raihan","Malek","Soyeb"]
print(list)
print(len(list))

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1[3])
print(list1[-3])

list1[3] ="15"
print(list1[3])

list3 = ["Apple","Mango","Banana","Orange"]
list3.append("Fruits")
print(list3)

list3.insert(1,"Totota")
print(list3)

car = ["toyota","Odi","Ferari","Corola"]
car.pop(1)
print(car)

car.remove("toyota")
print(car)

car.pop()
print(car)

car.clear
print(car)

game = ["Foodball","Cricket", "Badminton","Hocky"]
khela = game.copy()
print(khela)

list4 = [1,3,5,7,9]
list5 = [2,4,6,8,10]
list6 = list4 + list5
print(list6)

list4.extend(list5)
print(list4)
game = ["Foodball","Cricket", "Badminton","Hocky"]
game1 = game[2:3]
print(game1)