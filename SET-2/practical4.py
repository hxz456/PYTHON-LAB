import csv

subject = "English"
marks = []
with open("student.csv") as file:

    data = csv.DictReader(file)

    for i in data:
        marks.append(int(i[subject]))

print(f"Average of {subject} = {sum(marks)/len(marks)}")