
import time

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBUZZ")
            time.sleep(1)
        elif i % 3 == 0:
            print("Fizz")
            time.sleep(1)
        elif i % 5 == 0:
            print("Buzz")
            time.sleep(1)
        else:
            print(i)   
            time.sleep(1)

fizzbuzz()