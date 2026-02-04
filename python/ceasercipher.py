def caesar_encrypt(text, key):
    result = ""

    for char in text:
        if char.isupper():
            # A = 0 → Z = 25
            value = ord(char) - ord('A')
            new_value = (value + key) % 26
            result += chr(new_value + ord('A'))

        elif char.islower():
            value = ord(char) - ord('a')
            new_value = (value + key) % 26
            result += chr(new_value + ord('a'))

        else:
            result += char  

    return result

# Example usage:
if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    key = int(input("Enter key value number: "))
    encrypted_text = caesar_encrypt(text, key)
    decrypted_text = caesar_encrypt(encrypted_text, -key)
    print(f"Original: {text}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")