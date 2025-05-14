import random
import string


def generate_password(length=12):
    """Generate a random password with the given length."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password has at least one character from each pool
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return "".join(password)
    # Example usage


if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(password_length))
