import numpy as np

def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()

    # pad if length is odd
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
    det = int(np.linalg.det(key)) % 26
    det_inv = mod_inverse(det, 26)

    if det_inv is None:
        raise ValueError("Key matrix is not invertible!")

    # adjoint matrix
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


key = np.array([
    [3, 3],
    [2, 5]
])

msg = input("Enter the String to be encrypted: ")

cipher = encrypt(msg, key)
print("Encrypted:", cipher)

plain = decrypt(cipher, key)
print("Decrypted:", plain)

