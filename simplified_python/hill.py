# Hill Cipher (2x2) - Simple Pure Python Implementation

# Function to perform matrix multiplication on letter pairs
def hill_encrypt(msg, key):
    # Padding: message must be even length for 2x2 matrix
    if len(msg) % 2 != 0: 
        msg += "X"
    msg = msg.upper()
    cipher = ""
    
    # Process characters in blocks of 2
    for i in range(0, len(msg), 2):
        # Convert pair of letters to numbers (A=0, B=1...)
        p1, p2 = ord(msg[i]) - 65, ord(msg[i+1]) - 65
        
        # Multiply (key_row by plaintext_column) mod 26
        # Row 1: [a, b] * [p1, p2]
        c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
        # Row 2: [c, d] * [p1, p2]
        c2 = (key[1][0] * p1 + key[1][1] * p2) % 26
        
        # Convert resulting numbers back to letters
        cipher += chr(c1 + 65) + chr(c2 + 65)
    return cipher

# --- Main Execution ---
print("Enter 2x2 Key Matrix elements:")
# Taking key as a, b for row 1 and c, d for row 2
a = int(input("a (0,0): "))
b = int(input("b (0,1): "))
c = int(input("c (1,0): "))
d = int(input("d (1,1): "))
key = [[a, b], [c, d]]

msg = input("Enter plaintext: ")

# Execute encryption
encrypted = hill_encrypt(msg, key)
print(f"Encrypted: {encrypted}")
