def check_password_policy(password):
    """Validate password based on security rules."""
    if len(password) < 8:
        return "Password too short! Must be at least 8 characters."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    return "Password is strong!"

if __name__ == "__main__":
    password = input("Enter a password to validate: ")
    print(check_password_policy(password))
