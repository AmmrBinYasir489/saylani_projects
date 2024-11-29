import random
import string

def generate_password(length):
    lowercase = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    uppercase = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = string.digits              # '0123456789'
    special_characters = string.punctuation  # Special characters like !@#$%^&*


    all_characters = lowercase + uppercase + digits + special_characters

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return ''.join(password)

length = int(input("Enter the desired password length (minimum 4): "))
password = generate_password(length)
print(f"Generated password: {password}")