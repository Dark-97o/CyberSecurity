import numpy as np
import time

def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()

    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    cipher = ""

    for i in range(0, len(plaintext), 2):
        pair = np.array([
            ord(plaintext[i]) - 65,
            ord(plaintext[i+1]) - 65
        ])

        result = np.dot(key, pair) % 26

        cipher += chr(result[0] + 65)
        cipher += chr(result[1] + 65)

    return cipher


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()

    det = int(round(np.linalg.det(key))) % 26
    det_inv = mod_inverse(det, 26)

    if det_inv is None:
        raise ValueError("Key matrix is NOT invertible mod 26")

    adj = np.array([
        [ key[1][1], -key[0][1]],
        [-key[1][0],  key[0][0]]
    ]) % 26

    key_inv = (det_inv * adj) % 26

    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        pair = np.array([
            ord(ciphertext[i]) - 65,
            ord(ciphertext[i+1]) - 65
        ])

        result = np.dot(key_inv, pair) % 26

        plaintext += chr(int(result[0]) + 65)
        plaintext += chr(int(result[1]) + 65)

    return plaintext

def input_key():
    print("==========================")
    print("\nEnter 2×2 key matrix values:")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))

    return np.array([[a, b], [c, d]])


# ---------- MAIN ----------
key = input_key()

while True:
    print("==========================")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        msg = input("Enter plaintext: ")
        print("Encrypting...")
        time.sleep(0.8)
        print("Encrypted:", encrypt(msg, key))
        time.sleep(0.8)

    elif ch == 2:
        cipher = input("Enter ciphertext: ")
        print("Decrypting...")
        time.sleep(0.8)
        try:
            print("Decrypted:", decrypt(cipher, key))
        except ValueError as e:
            print("Error:", e)
        time.sleep(0.8)

    elif ch == 3:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
