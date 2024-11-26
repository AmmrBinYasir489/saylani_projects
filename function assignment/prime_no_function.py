def prime (number):
    is_prime = True
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
    elif number == 1:
        is_prime = True
    else:
        is_prime = False
    return is_prime

enter_number = int(input("enter the number to check if it is prime or not: "))
if prime(enter_number):
    print(f"{enter_number} is prime number.")
else:
    print(f"{enter_number} is not a prime number.")