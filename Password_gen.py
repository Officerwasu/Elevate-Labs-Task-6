import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected.")

    # Ensure at least one of each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the rest
    password += random.choices(characters, k=length - len(password))
    random.shuffle(password)

    return ''.join(password)

# Generate sample passwords of different strengths
print("Strong Password:", generate_password(16, True, True, True, True))
print("Medium Password:", generate_password(12, True, True, True, False))
print("Weak Password:", generate_password(8, True, False, False, False))
