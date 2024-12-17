import hashlib

def hash_password(password):
    """Hash a password using SHA-256."""
    password_bytes = password.encode('utf-8')
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    return hashed_password

if __name__ == "__main__":
    password = input("Enter a password to hash: ")
    print(f"SHA-256 Hashed Password: {hash_password(password)}")
