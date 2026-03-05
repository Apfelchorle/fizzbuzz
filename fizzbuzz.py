import time
import sys
from webbrowser import open
from os import write




# Functions


'loading animation'
def loading(text, delay=0.5):
    print(text, end="")

    for _ in range(3):
        time.sleep(delay)
        print(".", end="", flush=True)
    print("")



'base division'
def divise(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    print(divisors)

'sort through all the divisors, and replace with Fizz/Buzz/FizzBuzz'
def fizzbuzz(numb):
    global array
    array = []
    loading("fizzing n' buzzing")
    for i in range(1, numb + 1):
        array.append("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i or "FizzBuzz" * (i % 15 == 0))
    return array


'loop until given an integer'
while True:
    try:
        n = int(input("Number: "))
        break
    except ValueError:
        print("Please enter a valid integer.")


'function calls'
divise(n)
fizzbuzz(n)
print(array)

'program exit'
time.sleep(0.25)
loading("made by cqnstantine on github", 0.25)
open('https://www.github.com/Apfelchorle')


'I know this code is poorly optimized and all but who cares'


# using singe quotes as comments is fun