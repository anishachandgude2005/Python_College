from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9,10]
squares=list(map(lambda x:x*x,numbers))
even_numbers=list(filter(lambda x:x%2==0,numbers))
sum_of_numbers=reduce(lambda x,y:x+y,numbers)
print("Squares:",squares)
print("Even Numbers:",even_numbers)
print("Sum:",sum_of_numbers)