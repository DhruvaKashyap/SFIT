import hashlib

def hash_string(string):
    # Create a new SHA-1 hash object
    sha1_hash = hashlib.sha1()

    # Convert the string to bytes and update the hash object
    sha1_hash.update(string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_string = sha1_hash.hexdigest()

    return hashed_string