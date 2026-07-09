import string

def encrypt(text, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    encrypted = ""

    for char in text:
        if char.isalpha():
            position = alphabet.index(char.lower())
            new_char = key[position]

            if char.isupper():
                encrypted += new_char.upper()
            else:
                encrypted += new_char
        else:
            encrypted += char

    return encrypted


def decrypt(text, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    decrypted = ""

    for char in text:
        if char.isalpha():
            position = key.index(char.lower())
            original_char = alphabet[position]

            if char.isupper():
                decrypted += original_char.upper()
            else:
                decrypted += original_char
        else:
            decrypted += char

    return decrypted


print("===== Substitution Cipher =====")
print("Alphabet:", string.ascii_lowercase)

secret_key = input("Enter the 26-letter key: ").lower()

if len(secret_key) != 26 or not secret_key.isalpha():
    print("Invalid Key! Please enter exactly 26 alphabetic characters.")
else:
    plaintext = input("Enter the text to encrypt: ")

    cipher = encrypt(plaintext, secret_key)
    print("\nEncrypted Text:", cipher)

    original = decrypt(cipher, secret_key)
    print("Decrypted Text:", original)


'''
    Output
    
    ===== Substitution Cipher =====
    Alphabet: abcdefghijklmnopqrstuvwxyz
    Enter the 26-letter key: IAMFROKPGNBCDEHJLQSTUVWXYZ
    Enter the text to encrypt: I am the student of Sanjivani University

    Encrypted Text: G id tpr stufret ho Siengvieg Uegvrqsgty
    Decrypted Text: I am the student of Sanjivani University

'''