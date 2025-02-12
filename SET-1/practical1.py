
choice = -1
while True:
    print("\n1. Fahrenheit To Celsius")
    print("2. Celsius To Fahrenehit")
    print("0. Exit")

    choice = int(input("\nEnter Choice : "))
    fh , c = -1,-1
    if choice == 1:
        fh = float(input("\nEnter Temperature in Fahrenheit : "))
        c = (fh-32) / 1.8
        print("Temperature In Celsius is = " , c)
    
    elif choice == 2:
        c = float(input("\nEnter Temperature in Celsius : "))
        fh = (c * 1.8) + 32
        print("Temperature In Fahrenehit is = " , fh)

    else:
        break

    
"""
Basic Program with no loops and no repition

# Fahrenheit to Celsius
fh = float(input("Enter temperature in Fahrenheit: "))
celsius = (fh - 32) / 1.8
print("Temperature in Celsius =", celsius)

# Celsius to Fahrenheit
c = float(input("\nEnter temperature in Celsius: "))
fahrenheit = (c * 1.8) + 32
print("Temperature in Fahrenheit =", fahrenheit)

"""
        