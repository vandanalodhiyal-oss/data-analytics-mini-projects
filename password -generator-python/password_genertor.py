#user input----
length = int(input("Enter password length:"))

#Characters manually define ------
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

use_numbers = input("Include numbers? (yes/no): ")
use_symbols = input("Include symbols? (yes/no): ")

# Final characters set-----
all_chars = letters

if use_numbers == "yes":
    all_chars = all_chars + numbers

if use_symbols == "yes":
    all_chars = all_chars + symbols


password = ""

for i in range(length):
    index = i % len(all_chars)   # index generate karna
    password = password + all_chars[index]

print("Generated Password:", password)

# Strength check
if length >= 8:
    print("Strength: Strong")
else:
    print("Strength: Weak")