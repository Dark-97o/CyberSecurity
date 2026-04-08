# Vigenere Cipher - Easiest Implementation
def vigenere(text, key, encrypt=True):
    result = ""
    key = key.upper()
    text = text.upper()
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            if not encrypt: shift = -shift
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

# Taking input from user
msg = input("Enter message: ")
key = input("Enter keyword: ")

cipher = vigenere(msg, key)
print(f"Encrypted: {cipher}")
print(f"Decrypted: {vigenere(cipher, key, False)}")
