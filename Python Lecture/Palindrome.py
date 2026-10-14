#Accept the name and check if itd palindrome
name=input("Enter a name:")
flag=0
for i in range(len(name)//2):
    if name[i]!=name[len(name)-i-1]:
        flag=1
        break

if flag==1:
    print("Given string is not palindrome")
else:
    print("Given string is palindrome")



