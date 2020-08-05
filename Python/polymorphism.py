# - Duck Typing (Like Interface in Java)
# - Operator Overloading
# - Method Overloading (Not built-in in Python)
# - Method Overriding

class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Spelling")

class Laptop:
    def code(self, ide):
        ide.execute()


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(self.m1, self.m2)

    # sum overloading(1, 2, or 3 args) -> same name but different number of args
    def sum(self, a = None, b = None, c = None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s

# show() in B overrode show() in

class A:
    def show(self):
        print("show in A")

class B(A):
    def show(self):
        print("show in B")

a1 = B()
a1.show()

# s1 = Student(58,69)
# s2 = Student(60,65)
# s3 = s1 + s2

# if s1 > s2:
#     print("s1 wins")
# else:
#     print("s2 wins")

# print(s1.sum(5, 4, 9))
#print(s3.m1)
#ide = MyEditor()
#ide.execute()
