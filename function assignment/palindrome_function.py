def palindrome(string):
    is_palindrome = False
    str = string[::-1]
    if str == string:
        is_palindrome = True
    return is_palindrome
strr = input("enter the string: ")  
print(f"the string {strr} is palindrome ? {palindrome(strr)}")