# Caesar Cipher Implementation

def encrypt(text, shift):
    encrypted = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += ch

    return encrypted


def decrypt(text, shift):
    return encrypt(text, -shift)


print("===== Caesar Cipher Program =====")

plaintext = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

ciphertext = encrypt(plaintext, shift)
print("\nEncrypted Text:", ciphertext)

original = decrypt(ciphertext, shift)
print("Decrypted Text:", original)


'''
Output: 1
===== Caesar Cipher Program =====
Enter the text: Hello I am Tushar
Enter the shift value: 4

Encrypted Text: Lipps M eq Xywlev
Decrypted Text: Hello I am Tushar

=======================================

Output: 2
Enter the text: I love India
Enter the shift value: 6

Encrypted Text: O rubk Otjog
Decrypted Text: I love India

'''