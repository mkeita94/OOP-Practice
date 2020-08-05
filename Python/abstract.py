# Cannot create an instance of an abstract class
# Abstraction in Python
# ABC- Abstract Base 
# All classes that extend or inherit an abstract class 
# should implements all the methods in in the abstract class
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("It's running")

class Phone(Computer):
    def process(self):
        print("Processing phone data")

ph = Phone()
#com = Computer()
com1 = Laptop()
com1.process()