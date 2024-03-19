# Otevření souboru message.txt
with open("message.txt", "r") as file:
    plaintext = file.read()


# Caesarova šifra
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.isnumeric():
            result += chr((ord(char) - 48 + shift) % 10 + 48)
        else:
            result += char
    return result


ciphertext = caesar_cipher(plaintext, 1)

# Uložení zašifrované zprávy do souboru message_.txt
with open("message_.txt", "w") as file:
    file.write(ciphertext)
