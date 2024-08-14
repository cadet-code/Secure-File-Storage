import hashlib

def compute_file_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_file_integrity(file_path, original_hash):
    current_hash = compute_file_hash(file_path)
    return current_hash == original_hash
