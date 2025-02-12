def decimal_others(value, choice):
    if choice == 1:
        return value
    elif choice == 2:
        return bin(value)
    elif choice == 3:
        return oct(value)
    elif choice == 4:
        return hex(value)
    else:
        return "Invalid Option"


def binary_others(value, choice):
    decimal_value = int(value, 2)
    if choice == 1:
        return decimal_value
    elif choice == 2:
        return value
    elif choice == 3:
        return oct(decimal_value)
    elif choice == 4:
        return hex(decimal_value)
    else:
        return "Invalid Option"


def octal_others(value, choice):
    decimal_value = int(value, 8)
    if choice == 1:
        return decimal_value
    elif choice == 2:
        return bin(decimal_value)
    elif choice == 3:
        return value
    elif choice == 4:
        return hex(decimal_value)
    else:
        return "Invalid Option"


def hex_others(value, choice):
    decimal_value = int(value, 16)
    if choice == 1:
        return decimal_value
    elif choice == 2:
        return bin(decimal_value)
    elif choice == 3:
        return oct(decimal_value)
    elif choice == 4:
        return value.upper()
    else:
        return "Invalid Option"



while True:
    print("Select the base of your number:")
    print("[1] Decimal")
    print("[2] Binary")
    print("[3] Octal")
    print("[4] Hexadecimal")
    print("[5] Exit")
    input_choice = int(input("Enter your choice: "))

    if input_choice == 5:
        break

    if input_choice == 1:
        value = int(input("Enter decimal number: "))
    elif input_choice == 2:
        value = input("Enter binary number: ")
    elif input_choice == 3:
        value = input("Enter octal number: ")
    elif input_choice == 4:
        value = input("Enter hexadecimal number: ")
    else:
        print("Invalid base choice")
        break

    while True:
        print("target base :")
        print("[1] Decimal")
        print("[2] Binary")
        print("[3] Octal")
        print("[4] Hexadecimal")
        print("[5] Back to main menu")
        target_choice = int(input("Enter target conversion: "))

        if target_choice == 5:
            break

        print("Converted value:", end=" ")
        if input_choice == 1:
            print(decimal_others(value, target_choice))
        elif input_choice == 2:
            print(binary_others(value, target_choice))
        elif input_choice == 3:
            print(octal_others(value, target_choice))
        elif input_choice == 4:
            print(hex_others(value, target_choice))
        else:
            print("Invalid Option")