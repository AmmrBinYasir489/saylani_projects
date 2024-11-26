def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
enter_number = int(input("Enter the number to find its factorial: "))
print(f"The factorial of {enter_number} is {factorial(enter_number)}.")
