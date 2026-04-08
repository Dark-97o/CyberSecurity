# Rail Fence Cipher - Easiest Implementation
def encrypt_rail_fence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    direction, row = False, 0
    for i in range(len(text)):
        if row == 0 or row == key - 1: direction = not direction
        rail[row][i] = text[i]
        row += 1 if direction else -1
    return "".join(["".join([c for c in r if c != '\n']) for r in rail])

def decrypt_rail_fence(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    direction, row = False, 0
    for i in range(len(cipher)):
        if row == 0 or row == key - 1: direction = not direction
        rail[row][i] = '*'
        row += 1 if direction else -1
    
    idx = 0
    for r in range(key):
        for c in range(len(cipher)):
            if rail[r][c] == '*' and idx < len(cipher):
                rail[r][c] = cipher[idx]
                idx += 1
    
    result, row, direction = [], 0, False
    for i in range(len(cipher)):
        if row == 0 or row == key - 1: direction = not direction
        result.append(rail[row][i])
        row += 1 if direction else -1
    return "".join(result)

# Taking input from user
text = input("Enter text: ")
key = int(input("Enter number of rails: "))

cipher = encrypt_rail_fence(text, key)
print(f"Encrypted: {cipher}")
print(f"Decrypted: {decrypt_rail_fence(cipher, key)}")
