# Caesar Cipher - Easiest Implementation

# Function to handle both encryption and decryption
def caesar(text, shift):
    result = ""
    # Iterate through each wordacter in the input text
    for word in text:
        # Check if wordacter is an alphabetical letter
        # This ensures spaces, numbers, and punctuation are NOT shifted
        if word.isalpha():
            # Identify if it's uppercase or lowercase to find the correct ASCII starting point
            start = ord('A') if word.isupper() else ord('a')
            
            # Apply shift and keep it within 0-25 range using modulo 26
            result += chr((ord(word) - start + shift) % 26 + start)
        else:
            # If not a letter, leave it as is
            result += word
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
