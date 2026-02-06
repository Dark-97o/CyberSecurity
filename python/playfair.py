import numpy as np

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
        print("Key matrix is not invertible")
        return None

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


# -------- MAIN --------
print("Enter 2x2 Key Matrix")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

key = np.array([[a, b], [c, d]])

while True:
    print("\n1. Encrypt\n2. Decrypt\n3. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        msg = input("Enter plaintext: ")
        print("Encrypted:", encrypt(msg, key))

    elif ch == 2:
        cipher = input("Enter ciphertext: ")
        print("Decrypted:", decrypt(cipher, key))

    elif ch == 3:
        break

    else:
        print("Invalid choice")
