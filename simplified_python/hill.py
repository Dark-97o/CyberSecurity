# Hill Cipher (2x2) - Simple Pure Python Implementation

# Function to find modular inverse of a number mod m
def modInverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to encrypt text using the key matrix
def hill_encrypt(msg, key):
    # Padding: message must be even length for 2x2 matrix
    if len(msg) % 2 != 0: 
        msg += "X"
    msg = msg.upper()
    cipher = ""
    
    # Process characters in blocks of 2
    for i in range(0, len(msg), 2):
        p1, p2 = ord(msg[i]) - 65, ord(msg[i+1]) - 65
        c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
        c2 = (key[1][0] * p1 + key[1][1] * p2) % 26
        cipher += chr(c1 + 65) + chr(c2 + 65)
    return cipher

# Function to decrypt text by finding the matrix inverse
def hill_decrypt(cipher, key):
    # 1. Calculate the determinant (ad - bc)
    det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26
    
    # 2. Find the modular inverse of the determinant
    det_inv = modInverse(det, 26)
    if det_inv is None:
        return "Error: Key matrix is not invertible modulo 26"
    
    # 3. Find the Adjugate Matrix: [[d, -b], [-c, a]]
    adj = [[key[1][1], -key[0][1] % 26], [-key[1][0] % 26, key[0][0]]]
    
    # 4. Find Inverse Key Matrix: (det_inv * adj) % 26
    key_inv = [[(det_inv * adj[0][0]) % 26, (det_inv * adj[0][1]) % 26],
               [(det_inv * adj[1][0]) % 26, (det_inv * adj[1][1]) % 26]]
    
    # 5. Multiply ciphertext blocks by key_inv
    plaintext = ""
    for i in range(0, len(cipher), 2):
        c1, c2 = ord(cipher[i]) - 65, ord(cipher[i+1]) - 65
        p1 = (key_inv[0][0] * c1 + key_inv[0][1] * c2) % 26
        p2 = (key_inv[1][0] * c1 + key_inv[1][1] * c2) % 26
        plaintext += chr(p1 + 65) + chr(p2 + 65)
    return plaintext

# --- Main Execution ---
print("Enter 2x2 Key Matrix elements:")
a = int(input("a (0,0): "))
b = int(input("b (0,1): "))
c = int(input("c (1,0): "))
d = int(input("d (1,1): "))
key = [[a, b], [c, d]]

msg = input("Enter plaintext: ")

# Encrypt
encrypted = hill_encrypt(msg, key)
print(f"Encrypted: {encrypted}")

# Decrypt
decrypted = hill_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
