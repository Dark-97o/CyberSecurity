import time

def format_text(text):
    return text.replace(" ", "").upper()

def generate_key(text, key):
    key = key.upper()
    key_extended = ""
    j = 0

    for i in range(len(text)):
        if text[i].isalpha():
            key_extended += key[j % len(key)]
            j += 1
        else:
            key_extended += text[i]

    return key_extended

def encrypt(plaintext, key):
    plaintext = format_text(plaintext)
    key = generate_key(plaintext, key)

    cipher = ""
    for p, k in zip(plaintext, key):
        c = (ord(p) - 65 + ord(k) - 65) % 26
        cipher += chr(c + 65)

    return cipher

def decrypt(ciphertext, key):
    ciphertext = format_text(ciphertext)
    key = generate_key(ciphertext, key)

    plaintext = ""
    for c, k in zip(ciphertext, key):
        p = (ord(c) - 65 - (ord(k) - 65)) % 26
        plaintext += chr(p + 65)

    return plaintext


last_cipher = None  # stores last encrypted text

while True:
    print("==========================")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        msg = input("Enter plaintext: ")
        key = input("Enter keyword: ")
        print("Encrypting...")
        time.sleep(0.8)

        last_cipher = encrypt(msg, key)
        print("Encrypted:", last_cipher)
        time.sleep(0.8)

    elif ch == 2:
        if last_cipher:
            print("1. Use existing ciphertext")
            print("2. Enter new ciphertext")
            opt = int(input("Choose option: "))

            if opt == 1:
                cipher = last_cipher
                print("Using existing ciphertext:", cipher)
            elif opt == 2:
                cipher = input("Enter ciphertext: ")
            else:
                print("Invalid option!")
                continue
        else:
            print("No existing ciphertext found.")
            cipher = input("Enter ciphertext: ")

        key = input("Enter keyword: ")
        print("Decrypting...")
        time.sleep(0.8)
        print("Decrypted:", decrypt(cipher, key))
        time.sleep(0.8)

    elif ch == 3:
        print("Program Terminated")
        break

    else:
        print("Invalid choice!")
