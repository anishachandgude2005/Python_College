#Append item in list
colors=["red","pink"]
print(colors.append("blue"))

#Insert
print(colors.insert(1,"yellow"))

#push
#pop
#----------------------------------------------------------------------------------------

#--------------------------------Functions-------------------------------------------------

#length
numbers=[1,2,3,4,5]
print(len(numbers))

#Sum
print(sum(numbers))

#sorted
print(sorted(numbers))
print(sorted(numbers,reverse=True))




#create list of 10 numbers and the display a sum of last 4 elements ,
# Remove the items from the list located at 2nd and 5th position ,
# print the difference  of highest and smallest number in the list, 
# Append a new element in the list which is half of the item appendend in 3rd position

numlist=[50,30,40,20,10,70,90,80,60]
print(sum(numlist))

print(numlist.pop(2))
print(numlist.pop(5))

print(max(numlist))
print(min(numlist))

print("difference  of highest and smallest number in the list:",max(numlist) - min(numlist))

print(numlist)

