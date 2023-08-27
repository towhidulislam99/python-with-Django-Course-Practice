number = int(input ("Please Enter the Value: "))

character_check = input("Give Check Character: ")

if character_check in str(number):
    print("The character " + character_check + " exists in the number.")
else:
    print("The character does not exist in the number.")
