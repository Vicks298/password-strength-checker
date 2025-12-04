from password_utils import check_password_strength, hash_password

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")

    # Check strength
    level, suggestions = check_password_strength(password)
    print(f"\nStrength: {level}")

    # Show suggestions if any
    if suggestions:
        print("\nSuggestions to improve your password:")
        for s in suggestions:
            print("- " + s)

    # Show SHA-256 hash
    print("\nSHA-256 Hash (example of secure storage):")
    print(hash_password(password))

if __name__ == "__main__":
    main()

