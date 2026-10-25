import math
def log_calculator():
    print ("Welcome to the logarithm lodge.")
    print ("What do you wish to calculate?")

    while True:

        #Argument Input
        try:
            argument = float(input("Enter the Argument: "))

        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if argument <= 0:
            print("The argument must be greater than zero(0).")
            continue

        #Base Input
        base = input("Enter the Base ('e' for Euler's Number): ")

        if base.lower() == 'e':
            base = math.e

        else:
            try:
                base = float(base)
            except ValueError:
                print("Error: Please enter a valid number.")
                continue

        if base <=0 or base == 1:
            print("The base must be greater than zero(0) and not one(1).")
            continue

        result = math.log(argument, base)

        print(f"The result is: {result:.4f}")
log_calculator()
