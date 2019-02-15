from cracker import crack
from encoder import encoder
from random import choice

def main():
    text = readFile("ciphers.txt")[0]
    encoded = encoder(text)
    key = encoded["key"]
    plainText = encoded["plain"]
    cipher = encoded["cipher"]

    keyMap = crack(cipher)
    # print(getUnfound(keyMap))
    for key in keyMap:
        print(key + ": " + str(keyMap[key]))

    print(getInitGuess(keyMap))


def readFile(fileName):
    with open(fileName) as file:
        lines = [line.rstrip() for line in file]

    return lines


def getDefinite(keyMap):
    definite = []

    for key in keyMap:
        if len(keyMap[key]) == 1:
            definite.append(keyMap[key][0])

    return definite



def getCounts(keyMap):
    definite = getDefinite(keyMap)
    counts = []

    for key in keyMap:
        if len(keyMap[key]) != 1:
            counts.append(len(keyMap[key]))

    return counts


def getInitGuess(keyMap):
    guess = list("__________________________")
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for key in keyMap:
        if len(keyMap[key]) == 1:
            index = alphabet.index(keyMap[key][0])
            guess[index] = key

    for i in range(1, 26):
        for key in keyMap:
            if len(keyMap[key]) == i:
                value = choice(keyMap[key])
                while value in guess:
                    value = choice(keyMap[key])
                index = alphabet.index(value)
                guess[index] = key

    print("".join(char for char in guess))
    print(alphabet)
    print("hi")


def getUnfound(keyMap):
    found = []
    unfound = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for key in keyMap:
        for char in keyMap[key]:
            if char not in found:
                found.append(char)

    for letter in alphabet:
        if letter not in found:
            unfound.append(letter)

    return unfound


main()
