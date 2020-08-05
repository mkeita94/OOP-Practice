from time import sleep
from threading import*

class Hello(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Hello")

class Hi(Thread):
    def run(self):
        for j in range(5):
            sleep(1)
            print("Hi")

s1 = Hello()
s2 = Hi()
s1.start()
sleep(0.2)
s2.start()