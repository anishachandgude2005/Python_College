count=0
with open("textfile.txt","r") as file:
    data=file.read()

    for ch in data:
        if ch.lower() in "aeiou":
            count+=1
print("Total vowels:",count)