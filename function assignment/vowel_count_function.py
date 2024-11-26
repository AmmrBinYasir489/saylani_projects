def vowels_count(string):
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}
    for character in string:
        if character in vowels:
            count += 1
    return count
enter_string = input("enter the string to count vowels: ")
print(f"total no of vowels in {enter_string} are {vowels_count(enter_string)}")