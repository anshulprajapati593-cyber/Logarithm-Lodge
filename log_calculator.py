import math
print ("Welcome to the logarithm lodge")
print ("What do you wish to calculate?")

while True:
    argument = float(input("Enter the Argument: "))
    base = input("Enter the Base ('e' for Euler's Number): ")

    if base.lower() == 'e':
        base = math.e
    else:
        base = float(base)

    result = math.log(argument, base)

    print (f"The result is: {result}")
