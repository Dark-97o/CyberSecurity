# Vigenere Cipher - Easiest Implementation

# Function to perform Vigenere encryption or decryption
def vigenere(text, key, encrypt=True):
    result = ""
    # Convert both to uppercase for simple math
    key = key.upper()
    text = text.upper()
    key_index = 0 # Tracks which character of the keyword to use
    
    for char in text:
        if char.isalpha():
            # Find the shift value based on the current key character (A=0, B=1...)
            shift = ord(key[key_index % len(key)]) - 65
            
            # If we are decrypting, we reverse the shift direction
            if not encrypt: 
                shift = -shift
            
            # Apply shift and keep it within A-Z range using modulo 26
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            
            # Only increment key pointer if we actually processed a letter
            key_index += 1
        else:
            # Append non-alphabet characters unchanged
            result += char
    return result

# --- Main Execution ---
# 1. Take inputs from the user
msg = input("Enter message: ")
key = input("Enter keyword: ")

# 2. Encrypt the message
cipher = vigenere(msg, key, encrypt=True)
print(f"Encrypted: {cipher}")

# 3. Decrypt the message back to original
decrypted = vigenere(cipher, key, encrypt=False)
print(f"Decrypted: {decrypted}")
