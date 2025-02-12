with open("data.txt") as file:
    total_words = len(file.read().split(" "))
    print(f"Word Count = {total_words}")
