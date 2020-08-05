# - Duck Typing (Like Interface in Java)
# - Operator Overloading
# - Method Overloading
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

a = "5"
b = "6"
print(a+b)
print(str.__add__(a,b))

#ide = MyEditor()
#ide.execute()
