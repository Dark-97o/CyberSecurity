# Digital Signature - Simple Implementation (RSA-based)

# Function to find the modular multiplicative inverse
def modInverse(e, phi):
    for x in range(1, phi):
        if (e * x) % phi == 1: return x
    return 1

# 1. Key Generation (Same as RSA)
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
# n is the modulus
n = p * q
# phi is Euler's totient function
phi = (p-1)*(q-1)

# public exponent e
e = int(input(f"Enter public exponent e (gcd(e, {phi})=1): "))
# d is the private exponent used for signing
d = modInverse(e, phi)

# 2. Signing Process (Performed by the Sender)
msg = int(input(f"Enter message number to sign (m < {n}): "))

# Signing: S = M^d mod N (Inverse of encryption)
signature = pow(msg, d, n)
print(f"Signature generated (using Private Key d): {signature}")

# 3. Verification Process (Performed by the Receiver)
# Receiver uses the Sender's Public Key (e, n) to compute: M' = S^e mod N
verified_msg = pow(signature, e, n)
print(f"Verified Message from signature (using Public Key e): {verified_msg}")

# Final Authenticity Check
if msg == verified_msg:
    print("Signature Valid! The message is authentic and the sender is verified.")
else:
    print("Signature Invalid! Warning: The message may be tampered or keys are incorrect.")
