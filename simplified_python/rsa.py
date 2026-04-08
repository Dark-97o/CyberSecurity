# RSA Algorithm - Simple Implementation
def gcd(a, b):
    while b: a, b = b, a % b
    return a

def modInverse(e, phi):
    for x in range(1, phi):
        if (e * x) % phi == 1: return x
    return 1

# Taking input from user
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
n = p * q
phi = (p - 1) * (q - 1)

print(f"n = {n}, phi = {phi}")
e = int(input(f"Enter e (1 < e < {phi} & gcd(e, phi)=1): "))
d = modInverse(e, phi)
print(f"Calculated d: {d}")

msg = int(input(f"Enter numeric message (m < {n}): "))
cipher = pow(msg, e, n)
plain = pow(cipher, d, n)

print(f"Encrypted: {cipher}")
print(f"Decrypted: {plain}")
