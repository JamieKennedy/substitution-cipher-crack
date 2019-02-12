import json
import encoder


def crack(cipher):
    englishPatterns = {}
    key = initMap()
    cleanCipher = cleanCipherText(cipher)
    wordList = cleanCipher.lower().split(" ")
    lengths = countLengths(wordList)

    for length in lengths:
        englishPatterns[length] = readJson("dictionaryLen" + str(length))

    for word in wordList:
        pattern = getPattern(word)
        #print(pattern)
        try:
            matches = englishPatterns[len(word)][pattern]
        except KeyError:
            continue
        #print(matches)

        wordMap = initMap()
        for i in range(len(word)):
            letterMatches = set([match[i] for match in matches])
            if not wordMap[word[i]]:
               for letter in letterMatches:
                   wordMap[word[i]].append(letter)
            else:
                for letter in letterMatches:
                    if letter not in wordMap[word[i]]:
                        wordMap[word[i]].append(letter)

        intersect(key, wordMap)
        cleanUp(key)
    fillInEmpty(key)
    return key


def fillInEmpty(keyMap):
    definite = getDefinite(keyMap)
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for char in definite:
        alphabet.remove(char)

    for key in keyMap:
        if not keyMap[key]:
            keyMap[key] = alphabet


def getDefinite(keyMap):
    definite = []

    for key in keyMap:
        if len(keyMap[key]) == 1:
            definite.append(keyMap[key][0])

    return definite


def cleanCipherText(cipher):
    cleanCipher = ""
    allowedChars = " abcdefghijklmnopqrstuvwxyz"

    for char in cipher:
        if char.lower() in allowedChars:
            cleanCipher += char

    return cleanCipher


def intersect(key, wordMap):
    for letter in key:
        if not key[letter]:
            key[letter] = wordMap[letter]
        else:
            if wordMap[letter]:
                key[letter] = commonElements(key[letter], wordMap[letter])


def commonElements(a, b):
    result = []
    for element in a:
        if element in b:
            result.append(element)

    return result


def cleanUp(key):
    definiteMatches = {}

    for letter in key:
        if len(key[letter]) == 1:
            definiteMatches[letter] = key[letter][0]

    for match in definiteMatches:
        for letter in key:
            if match != letter and definiteMatches[match] in key[letter]:
                key[letter].remove(definiteMatches[match])


def initMap():
    key = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        key[letter] = []

    return key


def getPattern(word):
    seenLetter = ""
    pattern = ""
    count = 0

    for char in word:
        if char not in seenLetter:
            seenLetter += char
            pattern += str(count)
            count += 1
        else:
            pattern += str(seenLetter.index(char))
        pattern += "."
    return pattern[:-1]


def countLengths(wordList):
    counts = []
    for word in wordList:
        if len(word) not in counts:
            counts.append(len(word))

    return counts


def readJson(fileName):
    jsonData = open("jsonDicts/" + fileName + ".json").read()
    return json.loads(jsonData)


def readFile(fileName):
    with open(fileName) as file:
        lines = [line.rstrip() for line in file]

    return lines


if __name__ == "__main__":
    text = readFile("ciphers.txt")[1]
    encoded = encoder.encoder(text)
    key = encoded["key"]
    plainText = encoded["plain"]
    cipher = encoded["cipher"]

    keyMap = crack(text)
