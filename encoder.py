from random import shuffle


def encoder(plainText):
    key = keyGen()
    cipher = encode(key, plainText)
    output = {"key": key, "plain": plainText, "cipher": cipher}
    return output


def keyGen():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    shuffle(alphabet)
    return "".join(char for char in alphabet)


def encode(key, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encodedCipher = ""

    for char in cipher:
        if char.lower() in alphabet:
            if char.lower() != char:
                encodedCipher += key[alphabet.index(char.lower())].upper()
            else:
                encodedCipher += key[alphabet.index(char)]
        else:
            encodedCipher += char

    return encodedCipher


if __name__ == "__main__":
    text = input("Plain text: ")
    encoded = encoder(text)
    for key in encoded:
        print(key + ": " + encoded[key])
