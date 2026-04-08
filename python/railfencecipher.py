import time

def encrypt_rail_fence(text, key):
    # Create the matrix to mark the rail positions
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    
    # Fill the rails in zigzag pattern
    direction = False
    row, col = 0, 0
    
    for char in text:
        if row == 0 or row == key - 1:
            direction = not direction
        
        rail[row][col] = char
        col += 1
        
        if direction:
            row += 1
        else:
            row -= 1
            
    # Read the rail row by row to get ciphertext
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

def decrypt_rail_fence(cipher, key):
    # Create the matrix to mark the rail positions
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    
    # Mark the places with '*' to know where to put cipher chars
    direction = False
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0 or row == key - 1:
            direction = not direction
        
        rail[row][col] = '*'
        col += 1
        
        if direction:
            row += 1
        else:
            row -= 1
            
    # Now fill the marked places with ciphertext characters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
                
    # Read matrix in zigzag pattern to get original text
    result = []
    direction = False
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0 or row == key - 1:
            direction = not direction
            
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
            
        if direction:
            row += 1
        else:
            row -= 1
    return "".join(result)

def main():
    last_cipher = None
    
    while True:
        print("\n--- Rail Fence Cipher ---")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        try:
            choice = input("Enter Choice: ")
            if choice == '1':
                text = input("Enter plaintext: ")
                key = int(input("Enter key (number of rails): "))
                if key < 2:
                    print("Key must be greater than 1.")
                    continue
                
                print("Encrypting...")
                time.sleep(0.5)
                last_cipher = encrypt_rail_fence(text, key)
                print(f"Ciphertext: {last_cipher}")
                
            elif choice == '2':
                if last_cipher:
                    print(f"1. Use last ciphertext ({last_cipher})")
                    print("2. Enter new ciphertext")
                    opt = input("Choice: ")
                    if opt == '1':
                        cipher = last_cipher
                    else:
                        cipher = input("Enter ciphertext: ")
                else:
                    cipher = input("Enter ciphertext: ")
                
                key = int(input("Enter key (number of rails): "))
                if key < 2:
                    print("Key must be greater than 1.")
                    continue
                
                print("Decrypting...")
                time.sleep(0.5)
                plaintext = decrypt_rail_fence(cipher, key)
                print(f"Decrypted text: {plaintext}")
                
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
