import random
import string
import secrets
import argparse
import sys
import time

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("-U", "--no-upper", action="store_false", help="Exclude uppercase letters")
    parser.add_argument("-L", "--no-lower", action="store_false", help="Exclude lowercase letters")
    parser.add_argument("-D", "--no-digits", action="store_false", help="Exclude digits")
    parser.add_argument("-S", "--no-special", action="store_false", help="Exclude special characters")

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_upper=args.no_upper,
            use_lower=args.no_lower,
            use_digits=args.no_digits,
            use_special=args.no_special
        )
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
if __name__ == "__main__":
    main()