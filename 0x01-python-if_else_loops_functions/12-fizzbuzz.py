#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{num} ", end="")