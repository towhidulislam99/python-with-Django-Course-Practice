class Animal:
    def speak(self):
        pass

class Dog (Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meao"
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())