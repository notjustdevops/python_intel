import math
"""

Recurtion Finctions

1. Hello
2. Hellow n times
3. Sum 1+2+3+4+5
4. Factorial 5! = 1*2*3*4*5 = 120
5. fido 0,1,1,2,3,5,8,13,21,34,55
"""

def hello(x):
    if x==0:
        return
    else:
        print("Hello World!")
        hello(x-1)

hello(0)


def sum(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x-1)

z = sum(0)
print(z)


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(8))


def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x < 0:
        return 0  # Handle negative values of x
    else:
        return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(4))






