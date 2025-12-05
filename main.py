from password_utils import check_password_strength, hash_password
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")

    # Check strength
    level, suggestions = check_password_strength(password)

    # Color output
    if level == "WEAK":
        color = Fore.RED
    elif level == "MEDIUM":
        color = Fore.YELLOW
    else:
        color = Fore.GREEN

    print(f"\nStrength: {color}{level}{Style.RESET_ALL}")

    # Show suggestions if any
    if suggestions:
        print("\nSuggestions to improve your password:")
        for s in suggestions:
            print("- " + s)

    # SHA-256 hash
    print("\nSHA-256 Hash (example of secure storage):")
    print(hash_password(password))

if __name__ == "__main__":
    main()


