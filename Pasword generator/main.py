import random
print('Welcom to my password generator')
chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890!@#$%^&*<>"?/'
number = input('Amount of password to generator: ')
number = int(number)
length = input('Input your password length : ')
length = int(length)
print('\nhere are your password')
for pwd in range(number):
    passwords =  ' '
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)