# Digital Signature - Simple Implementation (RSA-based)
def modInverse(e, phi):
    for x in range(1, phi):
        if (e * x) % phi == 1: return x
    return 1

# Taking input from user
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
n = p * q
phi = (p-1)*(q-1)

e = int(input(f"Enter public exponent e (gcd(e, {phi})=1): "))
d = modInverse(e, phi)

msg = int(input(f"Enter message number to sign (m < {n}): "))

# Signing (with Private Key)
signature = pow(msg, d, n)
print(f"Signature generated: {signature}")

# Verification (with Public Key)
verified_msg = pow(signature, e, n)
print(f"Verified Message from signature: {verified_msg}")

if msg == verified_msg:
    print("Signature Valid! Authenticity confirmed.")
else:
    print("Signature Invalid! Message may be tampered.")
