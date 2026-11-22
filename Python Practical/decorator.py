#Decorator Implementation
def execution_time(func):
    def inner(n):
        print("Python programming")
        func(n)
        print("Function Finished")
        return inner
@execution_time
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("Factorial:",fact)
factorial(5)
