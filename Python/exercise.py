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

# car1 = Car("blue", "20,000")
# car2 = Car("red", "30,000")
# car1.print_info()
# car2.print_info()

# g = GoldenRetriever("Bingo", 3)
# print(g.speak())

# Iterator
val = [7, 5, 4, 9]
it = iter(val)
print(it.__next__())

# Generator
def topten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1

values = topten()

for i in values:
    print(i)


# Exception
a = 5
b = 5

try:
    print(a/b)
except Exception as e:
    print("A number cannot be divided by zero", e)
finally:
    print("End of Block")


try:
    print(a/b)
except ZeroDivisionError as e:
    print("A number cannot be divided by zero", e)
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("Error")
finally:
    print("End of Block")