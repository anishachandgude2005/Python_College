def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b

gen = fibonacci(10)
for num in gen:
    print(num)
