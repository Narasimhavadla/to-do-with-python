import re

def check_password_strength(password):
    # Define criteria
    min_length = 8
    min_uppercase = 1
    min_lowercase = 1
    min_digits = 1
    min_special_chars = 1

    strength = 0

    # Check length
    if len(password) >= min_length:
        strength += 2
    elif len(password) >= 6:
        strength += 1

    # Check uppercase letters
    if len(re.findall(r'[A-Z]', password)) >= min_uppercase:
        strength += 1

    # Check lowercase letters
    if len(re.findall(r'[a-z]', password)) >= min_lowercase:
        strength += 1

    # Check digits
    if len(re.findall(r'\d', password)) >= min_digits:
        strength += 1

    # Check special characters
    if len(re.findall(r'[!@#$%^&*]', password)) >= min_special_chars:
        strength += 1

    return strength

# Example usage:
# password = "MyP@ssw0rd"
password = input("enter your password: ")
strength = check_password_strength(password)

if strength >= 4:
    print("Strong password")
elif strength >= 2:
    print("Medium password")
else:
    print("Weak password")
