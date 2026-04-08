# Cryptography Theory: How the Algorithms Work

This document explains the mathematical and logical principles behind each of the algorithms implemented in the `simplified_python` directory.

---

## 1. Caesar Cipher (Substitution)
The simplest and oldest form of encryption. It is a type of **substitution cipher** where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

- **Formula**:
    - **Encryption**: $E_n(x) = (x + n) \mod 26$
    - **Decryption**: $D_n(x) = (x - n) \mod 26$
    - *(where $x$ is the letter index and $n$ is the shift/key)*
- **Example**: 
    - **Plaintext**: `HELLO`, **Shift**: `3`
    - **Process**: 
        - H (7) + 3 = K (10)
        - E (4) + 3 = H (7)
        - L (11) + 3 = O (14)
        - L (11) + 3 = O (14)
        - O (14) + 3 = R (17)
    - **Ciphertext**: `KHOOR`
    - **Decryption**: `KHOOR` - 3 = `HELLO`

---

## 2. Vigenere Cipher (Polyalphabetic Substitution)
An evolution of the Caesar cipher that uses a keyword to dampen the effectiveness of frequency analysis. Each letter of the plaintext is shifted by the value of the corresponding letter in the key.

- **Formula**:
    - **Encryption**: $C_i = (P_i + K_{i \mod L}) \mod 26$
    - **Decryption**: $P_i = (C_i - K_{i \mod L}) \mod 26$
    - *(where $L$ is the length of the key)*
- **Example**:
    - **Plaintext**: `HELLO`, **Key**: `KEY`
    - **Encryption**:
        - H (7) + K (10) = 17 (R)
        - E (4) + E (4) = 8 (I)
        - L (11) + Y (24) = 35 % 26 = 9 (J)
        - L (11) + K (10) = 21 (V)
        - O (14) + E (4) = 18 (S)
    - **Ciphertext**: `RIJVS`
    - **Decryption**: R (17) - K (10) = 7 (H) ... and so on.

---

## 3. Rail Fence Cipher (Transposition)
A **transposition cipher** that doesn't change the characters but rearranges their order. It derives its name from the way the characters are written in a zigzag pattern on imaginary "rails."

- **Logic**:
    1. Write the message in a zigzag pattern across $N$ rows.
    2. Read off each row sequentially from top to bottom.
- **Example**: `HELLOWORLD` with 3 rails:
    ```
    H . . . O . . . D
    . E . L . W . R .
    . . L . . . O . .
    ```
    - **Encryption**: Read top row, then middle, then bottom: `HOD` + `ELWR` + `LO` = `HODELWRLO`
    - **Decryption**: Reconstruct the rails and fill the characters to retrieve `HELLOWORLD`.

---

## 4. Hill Cipher (Matrix Substitution)
A polygraphic substitution cipher based on **linear algebra**. It uses a matrix as the encryption key.

- **Formula**:
    - **Encryption**: $C = (K \cdot P) \mod 26$
    - **Decryption**: $P = (K^{-1} \cdot C) \mod 26$
    - *(where $P$ is a vector of plaintext letters and $K$ is the key matrix)*
- **Example** (2x2 Matrix):
    - **Plaintext**: `HI` -> Vector $P = \begin{bmatrix} 7 \\ 8 \end{bmatrix}$ (H=7, I=8)
    - **Key Matrix** $K = \begin{bmatrix} 3 & 3 \\ 2 & 5 \end{bmatrix}$
    - **Encryption**: 
        - $C_1 = (3 \times 7 + 3 \times 8) \mod 26 = (21 + 24) \mod 26 = 45 \mod 26 = 19$ (**T**)
        - $C_2 = (2 \times 7 + 5 \times 8) \mod 26 = (14 + 40) \mod 26 = 54 \mod 26 = 2$ (**C**)
    - **Ciphertext**: `TC`

---

## 5. RSA Algorithm (Asymmetric Encryption)
The most widely used asymmetric algorithm, based on the mathematical difficulty of **factoring the product of two large prime numbers**.

- **Steps**:
    1. Select two primes $p$ and $q$.
    2. Compute $n = p \times q$ and $\phi(n) = (p-1)(q-1)$.
    3. Choose $e$ such that $1 < e < \phi(n)$ and $gcd(e, \phi(n)) = 1$.
    4. Calculate $d$ such that $(d \times e) \mod \phi(n) = 1$ (Modular Inverse).
- **Public Key**: $(e, n)$ | **Private Key**: $(d, n)$
- **Encryption Example**:
    - Primes $p=3, q=11 \rightarrow n=33, \phi(n)=20$.
    - Choose $e=7$. Find $d$: $(7 \times d) \mod 20 = 1 \rightarrow d=3$.
    - **Message** $M = 5$.
    - **Ciphertext** $C = 5^7 \mod 33 = 78125 \mod 33 = 14$
    - **Decryption**: $M = 14^3 \mod 33 = 2744 \mod 33 = 5$ (Success!)

---

## 6. Diffie-Hellman Key Exchange
A protocol that allows two parties to establish a **shared secret key** over an insecure channel without actually sending the key itself.

- **Example**:
    - **Public**: $p=23, g=5$
    - **Alice Private** $a=6$: $A = 5^6 \mod 23 = 15625 \mod 23 = 8$
    - **Bob Private** $b=15$: $B = 5^{15} \mod 23 = 19$
    - **Key Calculation**:
        - Alice computes $19^6 \mod 23 = 2$
        - Bob computes $8^{15} \mod 23 = 2$
    - **Shared Secret**: $2$

---

## 7. Digital Signature (Authenticity)
Uses asymmetric encryption (usually RSA or ECDSA) to prove the **authenticity** and **integrity** of a message. It ensures the sender is who they claim to be and the message hasn't been modified.

- **Example**:
    - **Private Key** $d=3, n=33$. **Message** $M=5$.
    - **Sign**: $S = 5^3 \mod 33 = 125 \mod 33 = 26$
    - **Verify**: (Public Key $e=7$)
        - Check: $26^7 \mod 33$
        - Result: $5$ (Matches original message!)
