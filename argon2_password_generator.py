#!/usr/bin/env python3
"""
Argon2id Password Generator

This tool generates secure passwords based on a memorized master password and a service/website identifier,
using Argon2id as the key derivation function.
"""

import argon2
import argparse
import base64
import getpass
import string
import re
import secrets
import sys


def generate_password(master_password, service_identifier, length=16, 
                      use_uppercase=True, use_lowercase=True, 
                      use_digits=True, use_special=True, 
                      memory_cost=65536, time_cost=3, parallelism=4):
    """
    Generate a password using Argon2id key derivation.
    
    Args:
        master_password: The memorized master password
        service_identifier: The service or site identifier (e.g., "amazon", "github")
        length: Length of the generated password
        use_uppercase: Include uppercase letters
        use_lowercase: Include lowercase letters
        use_digits: Include digits
        use_special: Include special characters
        memory_cost: Argon2 memory parameter (in kibibytes)
        time_cost: Argon2 time cost parameter
        parallelism: Argon2 parallelism parameter
    
    Returns:
        A derived password of specified length and character set
    """
    # Combine master password and service identifier
    combined = f"{master_password}:{service_identifier}"
    
    # Create salt from service identifier (consistent for same service)
    salt = service_identifier.encode('utf-8')
    # Ensure salt is at least 8 bytes as required by Argon2
    if len(salt) < 8:
        salt = salt + b'\x00' * (8 - len(salt))
    
    # Use Argon2id to derive a secure key
    hasher = argon2.PasswordHasher(
        time_cost=time_cost,
        memory_cost=memory_cost,
        parallelism=parallelism,
        hash_len=32,
        salt_len=16,
        type=argon2.Type.ID
    )
    
    # Generate the hash and extract the raw bytes
    hash_value = hasher.hash(combined)
    # Extract the base64-encoded hash part (after the parameters)
    hash_parts = hash_value.split('$')
    raw_hash = base64.b64decode(hash_parts[-1])
    
    # Define character sets based on user preferences
    chars = ''
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?/~"
    
    if not chars:
        raise ValueError("At least one character set must be enabled")
    
    # Convert the raw hash to a password of the desired length and character set
    password = ''
    for i in range(length):
        # Use bytes from the raw hash to select characters
        index = raw_hash[i % len(raw_hash)] % len(chars)
        password += chars[index]
    
    # Ensure password meets required character sets
    # This ensures at least one character from each enabled set is included
    password_list = list(password)
    pos = 0
    
    if use_lowercase and not re.search(r'[a-z]', password):
        password_list[pos] = secrets.choice(string.ascii_lowercase)
        pos += 1
    
    if use_uppercase and not re.search(r'[A-Z]', password):
        password_list[pos] = secrets.choice(string.ascii_uppercase)
        pos += 1
    
    if use_digits and not re.search(r'\d', password):
        password_list[pos] = secrets.choice(string.digits)
        pos += 1
    
    if use_special and not re.search(r'[!@#$%^&*()-_=+\[\]{}|;:,.<>?/~]', password):
        password_list[pos] = secrets.choice("!@#$%^&*()-_=+[]{}|;:,.<>?/~")
        pos += 1
    
    return ''.join(password_list)


def main():
    parser = argparse.ArgumentParser(description='Generate secure passwords using Argon2id')
    parser.add_argument('-s', '--service', help='Service or website identifier')
    parser.add_argument('-l', '--length', type=int, default=16, help='Password length (default: 16)')
    parser.add_argument('--no-lowercase', action='store_true', help='Exclude lowercase letters')
    parser.add_argument('--no-uppercase', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-special', action='store_true', help='Exclude special characters')
    parser.add_argument('-m', '--memory', type=int, default=65536, help='Memory cost (default: 65536 KiB)')
    parser.add_argument('-t', '--time', type=int, default=3, help='Time cost (default: 3)')
    parser.add_argument('-p', '--parallelism', type=int, default=4, help='Parallelism (default: 4)')
    
    args = parser.parse_args()
    
    # Interactive mode if service not provided
    service = args.service
    if not service:
        service = input("Enter service/website identifier: ")
    
    # Get master password securely (not showing on screen)
    master_password = getpass.getpass("Enter your master password: ")
    
    # Generate and display the password
    try:
        password = generate_password(
            master_password=master_password,
            service_identifier=service,
            length=args.length,
            use_lowercase=not args.no_lowercase,
            use_uppercase=not args.no_uppercase,
            use_digits=not args.no_digits,
            use_special=not args.no_special,
            memory_cost=args.memory,
            time_cost=args.time,
            parallelism=args.parallelism
        )
        print(f"\nGenerated password for '{service}' (length: {args.length}):")
        print(password)
    except Exception as e:
        print(f"Error generating password: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main()) 