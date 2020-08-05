
#------------------------------------------#
# General Knowledge about OOP              #
# -Variables: Instance var and Class var   #
# -Methods: Instance methods, class methods#
#   Static methods                         #
# -Access: Accessors and Mutators          #
#------------------------------------------#


#With Constructor
class Computer:
    os = "Windows" # Class variable
    def __init__(self, cpu, ram):
        self.cpu = cpu # Instance var
        self.ram = ram # Instance var
    def print_info(self):
        print("The computer has {} and {}".format(self.cpu, self.ram))

    def compare(self, other):
        if self.cpu == other.cpu and self.ram == other.ram:
            return True
        else:
            return False


class Student:
    school = "UMD"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lap = self.Laptop()

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3
    # Getter
    def get_m1(self):
        return self.m1

    # Setter
    def set_m1(self, val):
        self.m1 = val

    def show(self):
            print(self.m1, self.m2, self.m3)

    @classmethod
    def getSchool(cls):     # Class method
        return cls.school

    @staticmethod
    def info():             # Static method
        print("This is a static method")

    # Inner class
    class Laptop:
        def __init__(self):
            self.brand = "DELL"
            self.cpu = "i8"
            self.ram = "8"

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student(34,67,32)
s2 = Student(89,32,12)
print(s1.avg()) # instance method
cmp1 = Computer("i7", "8GB")
cmp2 = Computer("i5", "16GB")
cmp3 = Computer("i7", "8GB")
print(cmp1.compare(cmp3))
#cmp1.print_info()
#Update class variable
Computer.os = "Unix"

s1.lap.show()
