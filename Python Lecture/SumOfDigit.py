num=int(input("Enter a Number:"))
sum=0
while(num!=0):
    r=num%10
    num=num//10
    sum=sum+r
print("Sum of digit:",sum)

