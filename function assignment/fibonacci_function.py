def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number = int(input("enter the number to find its fibonacci series "))
print(f"the fibonacci series of the number is {fibonacci(number)}")