class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def print_info(self):
        print("The {} car has {} miles.".format(self.color, self.mileage))


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound = "Bark"):
        return super().speak(sound)

car1 = Car("blue", "20,000")
car2 = Car("red", "30,000")
car1.print_info()
car2.print_info()

g = GoldenRetriever("Bingo", 3)
print(g.speak())