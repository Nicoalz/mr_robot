import random
import string

characters_possible = string.ascii_letters + string.digits

length = input("What length for your password ?")

while not length.isdigit() or length == '0':
    print("Please write the length with digits (above 0)")
    length = input("What length for your password ?")

length = int(length)

def password_generator(nb_of_characters):
    password = ''
    for i in range(nb_of_characters):
        password += ''.join(random.choice(characters_possible))
    return f"Here's your password of {nb_of_characters} characters : {password}"

print(password_generator(length))