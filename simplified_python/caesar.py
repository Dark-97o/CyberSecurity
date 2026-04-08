# Caesar Cipher - Easiest Implementation
def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# Taking input from user
text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encrypted = caesar(text, shift)
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {caesar(encrypted, -shift)}")
