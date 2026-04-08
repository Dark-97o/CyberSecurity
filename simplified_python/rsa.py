# RSA Algorithm - Simple Implementation


# Function to find the modular multiplicative inverse of e mod phi
def modInverse(e, phi):
    # Simply loops to find d such that (e * d) % phi == 1
    for x in range(1, phi):
        if (e * x) % phi == 1: return x
    return 1

# --- Main Execution ---
# 1. Setup Public/Private Keys
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
# n is the modulus for both public and private keys
n = p * q
# phi is the Euler's Totient function value
phi = (p - 1) * (q - 1)

print(f"n = {n}, phi = {phi}")

# 2. Choose public exponent e (must be coprime to phi)
e = int(input(f"Enter public exponent e -> (gcd(e, {phi})=1): "))

# 3. Calculate private exponent d
d = modInverse(e, phi)
print(f"Calculated d (Private Key): {d}")

# 4. Message Processing
msg = int(input(f"Enter numeric message (m < {n}): "))

# Encryption (with Public Key e, n): C = m^e mod n
cipher = pow(msg, e, n)
print(f"Encrypted message: {cipher}")

# Decryption (with Private Key d, n): M = c^d mod n
plain = pow(cipher, d, n)
print(f"Decrypted message: {plain}")
