# Rail Fence Cipher - Easiest Implementation

# Function to encrypt text using the zigzag rail pattern
def encrypt_rail_fence(text, key):
    # Create the grid with placeholders ('\n') for empty spots
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    
    # direction: True for down, False for up
    # row: current row being filled
    direction, row = False, 0
    
    # Fill the grid in a zigzag motion
    for i in range(len(text)):
        # Switch direction when hitting top or bottom rail
        if row == 0 or row == key - 1: direction = not direction
        rail[row][i] = text[i]
        row += 1 if direction else -1
        
    # Read the rails from top to bottom, ignoring empty placeholders
    return "".join(["".join([c for c in r if c != '\n']) for r in rail])

# Function to decrypt text by reconstructing the zigzag pattern
def decrypt_rail_fence(cipher, key):
    # Same zigzag logic to mark the character positions with '*'
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    direction, row = False, 0
    for i in range(len(cipher)):
        if row == 0 or row == key - 1: direction = not direction
        rail[row][i] = '*'
        row += 1 if direction else -1
    
    # Fill the marked positions '*' with the actual ciphertext characters row by row
    idx = 0
    for r in range(key):
        for c in range(len(cipher)):
            if rail[r][c] == '*' and idx < len(cipher):
                rail[r][c] = cipher[idx]
                idx += 1
    
    # Finally, read the grid in zigzag pattern to recover original text
    result, row, direction = [], 0, False
    for i in range(len(cipher)):
        if row == 0 or row == key - 1: direction = not direction
        result.append(rail[row][i])
        row += 1 if direction else -1
    return "".join(result)

# --- Main Execution ---
text = input("Enter text: ")
key = int(input("Enter number of rails: "))

# Encrypt and Decrypt
cipher = encrypt_rail_fence(text, key)
print(f"Encrypted: {cipher}")
print(f"Decrypted: {decrypt_rail_fence(cipher, key)}")
