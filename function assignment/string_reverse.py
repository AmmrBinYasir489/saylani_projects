def string_reverse(string):
    reversed_string = string[::-1]
    return reversed_string

enter_str = input("enter the string to reverse: ")
print(f"the reversed string is as follow {string_reverse(enter_str)}")