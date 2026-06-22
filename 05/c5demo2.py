class Animal:
    # default constructor
    def __init__(self):
        self.name = "Generic Animal"
        self.age = 5

    # parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # parameterized constructor with default value for age
    def __init__(self, name, age = 5):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} makes a sound.")

    def description(self):
        print(f"{self.name} is {self.age} years old.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")
    def speak(self, sound):
        print(f"{self.name} says {sound}.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

if __name__ == "__main__":
    generic_animal = Animal("Generic")
    generic_animal.speak()
    generic_animal.description()

    dog = Dog("Buddy", 3)
    dog.speak("Woof Woof")
    dog.description()

    cat = Cat("Whiskers", 2)
    cat.speak()
    cat.description()