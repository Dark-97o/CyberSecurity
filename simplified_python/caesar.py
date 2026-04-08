# Caesar Cipher - Easiest Implementation

# Function to handle both encryption and decryption
def caesar(text, shift):
    result = ""
    # Iterate through each wordacter in the input text
    for word in text:
            # Identify if it's uppercase or lowercase to find the correct ASCII starting point
            start = ord('A') if word.isupper() else ord('a')
            
            # 1. (ord(word) - start): Normalize letter to 0-25 range
            # 2. (+ shift): Apply the shift
            # 3. (% 26): Wrap around if it goes past 'Z' or 'z'
            # 4. (+ start): Convert back to original ASCII range
            result += chr((ord(word) - start + shift) % 26 + start)
    return result

# --- Main Execution ---
# 1. Take plaintext message from the user
text = input("Enter text: ")

# 2. Take shift value (key) from the user
shift = int(input("Enter shift value: "))

# 3. Perform Encryption using the shift
encrypted = caesar(text, shift)
print(f"Encrypted: {encrypted}")

# 4. Perform Decryption by using the negative of the shift
decrypted = caesar(encrypted, -shift)
print(f"Decrypted: {decrypted}")
