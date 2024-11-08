# Représentation numérique de l'alphabet
alphabet = {chr(65 + i): i for i in range(26)}

# Paramètres de chiffrement
key = alphabet['J']  # Clé k = J => 9
iv = alphabet['R']  # Vecteur d'initialisation iv = R => 17

# Cryptogramme à déchiffrer (texte chiffré donné)
ciphertext = "LUJSS EVIEA NZCNW RPSTF STULH U".replace(" ", "")


# Fonction de déchiffrement CBC
def decrypt_cbc_caesar(ciphertext, key, iv, alphabet):
    # Convertir chaque lettre chiffrée en sa représentation numérique
    cipher_numbers = [alphabet[char] for char in ciphertext]
    plaintext_numbers = []

    # Initialiser le bloc précédent avec le vecteur d'initialisation (iv)
    previous_cipher = iv

    # Déchiffrement en mode CBC
    for c in cipher_numbers:
        # P_i = (C_i ⊕ C_{i-1} ⊕ k) mod 26
        p = (c - key - previous_cipher) % 26
        plaintext_numbers.append(p)

        # Mettre à jour le bloc précédent pour le prochain tour
        previous_cipher = c

    # Convertir les nombres en lettres
    plaintext = ''.join(chr(65 + num) for num in plaintext_numbers)
    return plaintext


# Déchiffrer le cryptogramme
decrypted_text = decrypt_cbc_caesar(ciphertext, key, iv, alphabet)
print(decrypted_text)
