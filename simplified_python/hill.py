# Hill Cipher (2x2) - Simple Pure Python Implementation
def hill_encrypt(msg, key):
    if len(msg) % 2 != 0: msg += "X"
    msg = msg.upper()
    cipher = ""
    for i in range(0, len(msg), 2):
        p1, p2 = ord(msg[i]) - 65, ord(msg[i+1]) - 65
        c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
        c2 = (key[1][0] * p1 + key[1][1] * p2) % 26
        cipher += chr(c1 + 65) + chr(c2 + 65)
    return cipher

# Taking input from user
print("Enter 2x2 Key Matrix elements:")
a = int(input("a (0,0): "))
b = int(input("b (0,1): "))
c = int(input("c (1,0): "))
d = int(input("d (1,1): "))
key = [[a, b], [c, d]]

msg = input("Enter plaintext: ")
encrypted = hill_encrypt(msg, key)
print(f"Encrypted: {encrypted}")
