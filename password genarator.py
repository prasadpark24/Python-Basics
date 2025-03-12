import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_specialcharacter=True):
    
    characters = string.ascii_lowercase  
    
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_specialcharacter:
        characters += string.punctuation
    
    if length < 1:
        return "Password length must be at least 1."
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__== "_main_":
    print("Welcome to the Password Generator!")
    
  
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
   
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"Generated Password: {password}")