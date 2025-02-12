string = input("\nEnter String : ")

if string == string[::-1]:
    print(f"\nGiven String '{string}' is Palindrome")
else:
    print(f"\nGiven String '{string}' is not Palindrome")