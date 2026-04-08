# Diffie-Hellman Key Exchange - Simple Implementation

# 1. Agree on public parameters
p = int(input("Enter common prime p: ")) # Modulus
g = int(input("Enter common base g: ")) # Base (generator)

# 2. Alice's Part
a = int(input("Alice: Enter private key a: "))
# Public Key A = g^a mod p
A = pow(g, a, p) 
print(f"Alice's Public Key A (sent to Bob): {A}")

# 3. Bob's Part
b = int(input("Bob: Enter private key b: "))
# Public Key B = g^b mod p
B = pow(g, b, p) 
print(f"Bob's Public Key B (sent to Alice): {B}")

# 4. Exchange and Shared Secret calculation
# Alice takes Bob's public key B and calculates: S = B^a mod p
alice_secret = pow(B, a, p)

# Bob takes Alice's public key A and calculates: S = A^b mod p
bob_secret = pow(A, b, p)

# Both should now have the exact same secret value
print(f"Shared Secret (Alice calculates): {alice_secret}")
print(f"Shared Secret (Bob calculates): {bob_secret}")
