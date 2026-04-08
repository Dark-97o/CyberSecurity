# Diffie-Hellman Key Exchange - Simple Implementation
# Taking input from user
p = int(input("Enter common prime p: "))
g = int(input("Enter common base g: "))

# Alice's private key
a = int(input("Alice: Enter private key a: "))
A = pow(g, a, p) # Alice's public key
print(f"Alice's Public Key A: {A}")

# Bob's private key
b = int(input("Bob: Enter private key b: "))
B = pow(g, b, p) # Bob's public key
print(f"Bob's Public Key B: {B}")

# Shared Secret calculation
alice_secret = pow(B, a, p)
bob_secret = pow(A, b, p)

print(f"Shared Secret (Alice calculates): {alice_secret}")
print(f"Shared Secret (Bob calculates): {bob_secret}")
