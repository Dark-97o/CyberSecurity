import time

def calculate_shared_key(other_public, my_private, p):
    return pow(other_public, my_private, p)

def main():
    print("\n--- Diffie-Hellman Key Exchange ---")
    
    # Common public parameters
    p = int(input("Enter a large prime number (p): "))
    g = int(input(f"Enter a primitive root for {p} (g): "))
    
    print("\n--- Alice ---")
    alice_private = int(input("Alice: Enter your private key (a): "))
    alice_public = pow(g, alice_private, p)
    print(f"Alice's Public Key (A = g^a % p): {alice_public}")
    
    print("\n--- Bob ---")
    bob_private = int(input("Bob: Enter your private key (b): "))
    bob_public = pow(g, bob_private, p)
    print(f"Bob's Public Key (B = g^b % p): {bob_public}")
    
    print("\n--- Exchange Phase ---")
    print("Alice sends A to Bob...")
    time.sleep(0.5)
    print("Bob sends B to Alice...")
    time.sleep(0.5)
    
    print("\n--- Shared Secret Calculation ---")
    alice_shared_secret = calculate_shared_key(bob_public, alice_private, p)
    bob_shared_secret = calculate_shared_key(alice_public, bob_private, p)
    
    print(f"Alice calculates (B^a % p): {alice_shared_secret}")
    print(f"Bob calculates (A^b % p): {bob_shared_secret}")
    
    if alice_shared_secret == bob_shared_secret:
        print("\nSuccess! Shared secret matched.")
    else:
        print("\nFailure! Shared secrets do not match.")

if __name__ == "__main__":
    main()
