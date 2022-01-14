binary_imput = input("Enter the binary you want to convert into hexadecimal ?")

while len(binary_imput) % 4 != 0:
    print('The binary must be a number multiple of 4')
    binary_imput = input("Enter the binary you want to convert into hexadecimal ?")

p = set(binary_imput)
s = {'0', '1'}

while s != p and p != {'0'} and p != {'1'}:
    print('The binary must be written only with 0 and 1')
    binary_imput = input("Enter the binary you want to convert into hexadecimal ?")
    p = set(binary_imput)

def binary_to_hexa(binary_to_convert):
    return hex(int(f'{binary_to_convert}', 2))[2:]

print(binary_to_hexa(binary_imput))
