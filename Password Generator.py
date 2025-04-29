import random 

print('Let\'s create your password(s)!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&*().,?0123456789'  # Possible characters

number = int(input('What is the number of passwords you want? ')) # Number of passwords to generate

length = int(input("What is your password length? "))
       
print('\nhere are your passwords: ')
for _ in range(number):  # Using underscore (_) as a throwaway variable since we don't need the value
    passwords = '' # Initialize an empty string for each password
    for _ in range (length):
        passwords += random.choice(chars)  # Add a random character from chars to passwords
    print(passwords)