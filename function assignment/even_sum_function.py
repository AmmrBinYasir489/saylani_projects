def even_sum(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

number_list = [0, 4, 5, 6, 0]
print(f"The sum of even numbers in {number_list} is {even_sum(number_list)}")
