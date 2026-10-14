with open("textfile.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))

print("Second line:", lines[1].strip())
print("Fourth line:", lines[3].strip())