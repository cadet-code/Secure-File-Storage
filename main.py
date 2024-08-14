from authentication import authenticate_user, create_user
from encryption import encrypt_file, decrypt_file, generate_key
from accesscontrol import check_access, grant_access
from integrity import compute_file_hash, verify_file_integrity

def main():
    print("Secure File Storage System")
    # Example workflow
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if authenticate_user(username, password):
        print("Authentication successful.")
        
        # Key generation
        key = generate_key()
        
        # File operations
        file_path = "example.txt"
        encrypt_file(file_path, key)
        print("File encrypted.")
        
        # File access
        if check_access(username, 1):
            print("Access granted.")
            decrypt_file(file_path, key)
            print("File decrypted.")
            
            # Integrity check
            original_hash = compute_file_hash(file_path)
            if verify_file_integrity(file_path, original_hash):
                print("File integrity verified.")
            else:
                print("File integrity compromised.")
        else:
            print("Access denied.")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()
