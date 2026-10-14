with open("textfile.txt", "r") as file:
    data = file.read()

words = data.split()

print("Total words:", len(words))

unique_words = set(words)

print("Unique words:", unique_words)