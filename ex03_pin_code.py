import hashlib


def pin_code(password_hashed):
    print("Please wait a moment, the program is processing...")
    for i in range(100000000):
        password_to_hash = f'{i:08}' #Si j'utilise seulement i je n'aurai pas les nombres au format 00000001 etc...
        password_hash_test = hashlib.md5(password_to_hash.encode('utf-8')).hexdigest()
        if password_hash_test == str(password_hashed):
            return f"Your password is {password_to_hash}"
    return 'No match. Please verify your md5 hashed password and retry'

print(pin_code(input('What is your md5 hashed password ?')))