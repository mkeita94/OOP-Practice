# Inheritance
# - Single Level Inheritance
# - Multi Level Inheritance
# - Parent Constructor
# - MRO (Method Resolution Order) -> Left to Right
class A:
    def __init__(self):
        print("In A")
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")

class B(A): # Inherits from A -> Single Level
    def __init__(self):
        super().__init__()
        print("In B")
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")

class C(B):
    def feature5(self): # Inherits from B -> Multi Level
        print("Feature 5 working")

a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature3()
b1.feature4()
b1.feature2()
b1.feature1()
c1 = C()
c1.feature5()