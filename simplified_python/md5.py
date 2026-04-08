import hashlib

# MD5 Hashing - Easiest Implementation
# Note: MD5 is a hashing algorithm (one-way), not a cipher (reversible).

def generate_md5(text):
    # 1. Encode the string into bytes
    encoded_text = text.encode()
    
    # 2. Create an md5 hash object
    md5_hash = hashlib.md5(encoded_text)
    
    # 3. Return the hexadecimal representation of the digest
    return md5_hash.hexdigest()

# --- Main Execution ---
# 1. Take input from user
user_input = input("Enter string to hash: ")

# 2. Generate and print the hash
result = generate_md5(user_input)
print(f"MD5 Hash: {result}")

# 3. Explanation of one-way nature
print("\nNote: MD5 is a one-way hash. There is no 'decrypt' function for hashes.")
