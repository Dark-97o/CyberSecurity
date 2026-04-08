# Code-Level Logic: How the Python Scripts Work

This document explains the specific Python implementation details for each script in the `simplified_python` folder.

---

## 1. Caesar Cipher (`caesar.py`)
### Code Logic:
- **`ord()` and `chr()`**: We use `ord('A')` to get the numeric ASCII value (65) and `chr()` to convert it back.
- **Normalization**: By subtracting the starting ASCII (`ord('A')` or `ord('a')`), we bring the character into a 0-25 range.
- **Modulo Operation (`% 26`)**: This ensures that if a shift goes past 'Z', it "wraps around" back to 'A'.

```python
# The heart of the shift:
result += chr((ord(char) - start + shift) % 26 + start)
```

---

## 2. Vigenere Cipher (`vigenere.py`)
### Code Logic:
- **Key Cycling**: We use `key_index % len(key)` to repeatedly loop the keyword over the longer plaintext message.
- **Directional Shift**: The `encrypt` boolean toggle allows us to use the same logic for both encryption (adding shift) and decryption (subtracting shift).

```python
# Matching message char with key char:
shift = ord(key[key_index % len(key)]) - 65
```

---

## 3. Rail Fence Cipher (`railfence.py`)
### Code Logic:
- **Matrix / List of Lists**: A 2D list `rail` is used to represent the rows (rails).
- **Zigzag Direction**: A boolean `direction` flips whenever the "row marker" hits the top (0) or bottom (`key - 1`) rail.
- **List Comprehension**: Used to elegantly join all non-empty characters from the rails into a single ciphertext string.

```python
# Joining the rails row-by-row:
return "".join(["".join([c for c in r if c != '\n']) for r in rail])
```

---

## 4. Hill Cipher (`hill.py`)
### Code Logic:
- **Block Processing**: Since it's a 2x2 matrix, the code processes the text in pairs (`range(0, len(msg), 2)`).
- **Dot Product Simulation**: Instead of using heavy libraries like `numpy`, we manually perform the $1 \times 2$ by $2 \times 2$ matrix multiplication.

```python
# Manual matrix multiplication:
c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
c2 = (key[1][0] * p1 + key[1][1] * p2) % 26
```

---

## 5. RSA Algorithm (`rsa.py`)
### Code Logic:
- **Modular Exponentiation**: We use Python's built-in `pow(base, exp, mod)` function. This is highly optimized and much faster than `(base ** exp) % mod`.
- **Modular Inverse**: A simple loop finds the number `d` such that `(e * d) % phi == 1`.
- **GCD**: A standard recursive/while-loop implementation of the Euclidean algorithm to ensure `e` is valid.

```python
# RSA core math:
cipher = pow(msg, e, n)
plain = pow(cipher, d, n)
```

---

## 6. Diffie-Hellman (`diffie_hellman.py`)
### Code Logic:
- **Simultaneous Calculation**: The code calculates the public keys `A` and `B` independently, then uses the *other* person's public key to find the secret.
- **Shared Result**: It proves that `pow(B, a, p)` is identical to `pow(A, b, p)` because mathematically both equal $g^{ab} \mod p$.

---

## 7. Digital Signature (`digital_signature.py`)
### Code Logic:
- **Inverse RSA**: While RSA usually encrypts with the Public Key, signatures **Sign** with the **Private Key** (`d`).
- **Validation**: The verification step uses the **Public Key** (`e`) to return the signature to its original message state.

```python
# Sign with d (Private):
signature = pow(msg, d, n)

# Verify with e (Public):
verified_msg = pow(signature, e, n)
```
