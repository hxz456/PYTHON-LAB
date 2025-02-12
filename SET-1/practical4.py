# static method to calculate average of a list of numbers

#  a = [1,2,3,4,5,6,7,8,9,10]

# print("Average = " , sum(a)/len(a))


numbers = input("\nEnter the numbers separated by space: ")
numbers_list = numbers.split(" ")

sum = 0

for i in numbers_list:
    if i.isdigit():
        i = int(i)
        sum += i

print("Average = ", sum/len(numbers_list))