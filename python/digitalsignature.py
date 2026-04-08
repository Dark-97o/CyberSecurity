import time

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modInverse(e, phi):
    m0 = phi
    y = 0
    x = 1
    if phi == 1:
        return 0
    while e > 1:
        q = e // phi
        t = phi
        phi = e % phi
        e = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0
    return x

def sign(m, d, n):
    return pow(m, d, n)

def verify(s, e, n):
    return pow(s, e, n)

def main():
    print("\n--- Digital Signature Algorithm (RSA based) ---")
    
    # Key generation
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    n = p * q
    phi = (p-1) * (q-1)
    
    e = int(input(f"Enter e (gcd(e, {phi})==1): "))
    while gcd(e, phi) != 1:
        e = int(input("Invalid e! Enter again: "))
    
    d = modInverse(e, phi)
    
    print(f"\nPublic Key (for verification): (e={e}, n={n})")
    print(f"Private Key (for signing): (d={d}, n={n})")
    
    while True:
        print("\n1. Sign Message")
        print("2. Verify Signature")
        print("3. Exit")
        
        choice = input("Enter Choice: ")
        
        if choice == '1':
            msg = int(input(f"Enter message as a number (m < {n}): "))
            signature = sign(msg, d, n)
            print(f"Digital Signature generated: {signature}")
            
        elif choice == '2':
            signature = int(input("Enter signature to verify: "))
            original_msg = int(input("Enter original message number: "))
            
            e_verify = int(input("Enter sender's public key (e): "))
            n_verify = int(input("Enter sender's public key (n): "))
            
            decrypted_msg = verify(signature, e_verify, n_verify)
            
            print(f"Decrypted message from signature: {decrypted_msg}")
            
            if decrypted_msg == original_msg:
                print("\nVerification Successful! The message is authentic and untampered.")
            else:
                print("\nVerification Failed! The message may have been tampered with or the signature is invalid.")
                
        elif choice == '3':
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()
