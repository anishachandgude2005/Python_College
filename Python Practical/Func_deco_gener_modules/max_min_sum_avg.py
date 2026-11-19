def analyze_numbers(numbers):
    maximum=max(numbers)
    minimum=min(numbers)
    total=sum(numbers)
    average=total/len(numbers)

    print("maximum=",maximum)
    print("minimum=",minimum)
    print("Sum=",total)
    print("Average=",average)

numbers=[10,20,30,40]
analyze_numbers(numbers)

