import random
import string

s = string.ascii_letters + string.digits + string.punctuation

pwd = ""

length = int(input("Enter the length of the password: "))

for i in range(length):
    pwd += random.choice(s)

print(pwd)

print(random.choices(s,k=length))
print(random.sample(s,k=length))