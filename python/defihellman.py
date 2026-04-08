p = int(input("Enter prime number (p): "))
g = int(input("Enter generator (g): "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = (g ** a) % p
B = (g ** b) % p

print("Alice's Public Key:", A)
print("Bob's Public Key:", B)

secret_alice = (B ** a) % p
secret_bob = (A ** b) % p

print("Shared Secret computed by Alice:", secret_alice)
print("Shared Secret computed by Bob:", secret_bob)
