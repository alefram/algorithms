def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x-1)

x = factorial(5)
print("el factorial es:",x)
