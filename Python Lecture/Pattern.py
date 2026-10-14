for i in range(1,4):
    for j in range(i,i+1):
        if(i%2!=0):
            print("*"*j,end=" ")
        else:
            print("#"*j,end=" ")
    print()
        