import time

# Simple GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Modular Inverse using Extended Euclidean Algorithm
def modInverse(e, phi):
    m0 = phi
    y = 0
    x = 1
 
    if phi == 1:
        return 0
 
    while e > 1:
        # q is quotient
        q = e // phi
        t = phi
 
        # phi is remainder now, process same as
        # Euclid's algo
        phi = e % phi
        e = t
        t = y
 
        # Update y and x
        y = x - q * y
        x = t
 
    # Make x positive
    if x < 0:
        x = x + m0
 
    return x

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)

def main():
    print("\n--- RSA Algorithm ---")
    
    # Pre-selected primes for demonstration
    # In a real scenario, these would be large random primes
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    
    n = p * q
    phi = (p-1) * (q-1)
    
    print(f"n = {n}")
    print(f"phi(n) = {phi}")
    
    e = int(input(f"Enter e (1 < e < {phi} & gcd(e, {phi})==1): "))
    while gcd(e, phi) != 1:
        e = int(input(f"Invalid e! Enter e such that gcd(e, {phi})==1: "))
    
    d = modInverse(e, phi)
    print(f"Calculated d (Private Key component): {d}")
    
    print(f"\nPublic Key: (e={e}, n={n})")
    print(f"Private Key: (d={d}, n={n})")
    
    while True:
        print("\n1. Encrypt Message (Number)")
        print("2. Decrypt Message (Number)")
        print("3. Exit")
        
        choice = input("Enter Choice: ")
        
        if choice == '1':
            m = int(input(f"Enter message as a number (m < {n}): "))
            if m >= n:
                print(f"Error: message must be less than n={n}")
                continue
            c = encrypt(m, e, n)
            print(f"Encrypted message (Ciphertext): {c}")
            
        elif choice == '2':
            c = int(input("Enter ciphertext as a number: "))
            m = decrypt(c, d, n)
            print(f"Decrypted message (Plaintext): {m}")
            
        elif choice == '3':
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()
