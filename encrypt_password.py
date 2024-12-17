from cryptography.fernet import Fernet

def generate_key():
    """Generate a symmetric encryption key."""
    return Fernet.generate_key()

def encrypt_password(key, password):
    """Encrypt the password using the given key."""
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(key, encrypted_password):
    """Decrypt the password using the given key."""
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()

if __name__ == "__main__":
    key = generate_key()
    print(f"Generated Key: {key.decode()}")
    password = input("Enter a password to encrypt: ")
    encrypted_password = encrypt_password(key, password)
    print(f"Encrypted Password: {encrypted_password}")
    print(f"Decrypted Password: {decrypt_password(key, encrypted_password)}")
