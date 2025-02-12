while True:
    print("\nRectangle Calculator")
    print("1. Calculate Area\n2. Calculate Perimeter\n3. Exit")
    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        area = length * breadth
        print(f"Area of the rectangle: {area:.2f}")

    elif choice == "2":
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        perimeter = 2 * (length + breadth)
        print(f"Perimeter of the rectangle: {perimeter:.2f}")

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
