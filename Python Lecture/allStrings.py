text=" I am Anisha"
#1Strip spaces
print("Remove Spaces",text.strip())

#2 Uppercase
print("Upper Case:",text.upper())

#3Lower case
print("Lower Case",text.lower())

# 4Capitalize first letter
text=text.strip()
print("Capitalize first letter:",text.capitalize())

#5 Title Case (capitalize each word)
print(text.title())

#6 Count occurence of a substring
print("Letter C occurs",text.count("C"),"times in text")

#7 Find the position of substring(-1 if not found)
print("Position of am in text is",text.find("am"))

#8 Replace a substring
print(text.replace("Anisha","Good Girl"))

#9 Check if string start or ends with certain substring
print(text.startswith("I"))
print(text.endswith("Anisha"))

#split string into list by a delimeter



#
