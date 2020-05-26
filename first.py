#Going to make some Fibbin
import os
import warnings
warnings.filterwarnings("ignore")

# yes, I know this does not actually
# print out a Fibonacci Sequence and is just
# the factorial of a number
def fibonacci(n):
    x = 1
    if (x<n):
        x = fibonacci(n-1) * n
        return x
    else:
        return x

# let's ignore that and continue

print("Is this a fib?")
discard = input("Decide \n")
print("Kidding, it's Fibonacci.")
intToFib = input("Enter an integer \n")
try:
    newInt = int(intToFib)
except ValueError:
    print("Not cool, it wasn't an integer. No Fibonacci for you")
else:
    if (newInt < 1):
        print("Not cool, it wasn't a positive integer. No Fibonacci for you")
    else:
        print("The Fibonacci of ", newInt," is ", fibonacci(newInt))

# I promise that when I do serious work it's
# serious humor and function names are relevant