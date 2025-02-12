numbers = input("\nEnter the numbers separated by space: ")
numbers_list = numbers.split(" ")

for i in range(len(numbers_list)):
    if numbers_list[i].isdigit():
        numbers_list[i] = int(numbers_list[i])

numbers_list.sort()
print("Ascending Order: ", numbers_list)

numbers_list.sort(reverse=True)
print("Descending Order: ", numbers_list)
