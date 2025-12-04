import re
import hashlib

def check_password_strength(password):
    strength_points = 0
    suggestions = []

    # Length
    if len(password) >= 12:
        strength_points += 2
    elif len(password) >= 8:
        strength_points += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Numbers
    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        suggestions.append("Add numbers.")

    # Special characters
    if re.search(r"[^A-Za-z0-9]", password):
        strength_points += 1
    else:
        suggestions.append("Add special characters (!@#$%, etc).")

    # Strength label
    if strength_points <= 3:
        level = "WEAK"
    elif strength_points <= 5:
        level = "MEDIUM"
    else:
        level = "STRONG"

    return level, suggestions

def hash_password(password):
    """Return the SHA-256 hash of the password"""
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed
