import json
from re import sub


def main():
    englishPatterns = {}
    key = initMap()
    cipher = "uwqlhkvwyleq zsubxcmj hem xjm kf uksumybmc imjjyvmj uzlemwj ysc ukcmj, zhj lxwlkjm amzsv hk ybhmw hem fkwi kf y imjjyvm kw ukiixszuyhzks zs jxue y nyq heyh zh zj zshmbbzvzabm ksbq hk hem lmwjks lkjjmjjzsv hem gmq, uwqlhysybjzj zj hem awmygzsv kf hem ukcmj kw uzlemw nzhekxh hem gmq hmueszuybbq hemwm zj y jxahbm czffmwmsum amhnmms ukcmj ysc uzlemwj y ukcm zj ayjmc ks ukilbmhm ukilbmhm nkwcj kw lewyjmj nemwm ybb hem nkwcj ywm wmlbyumc aq ukcm nkwcj kw sxiamwj ysc y ukcm akkg zj smmcmc zs kwcmw fkw y imjjyvm hk am jmsh kw wmyc y uzlemw ks hem khemw eysc xjmj jzsvbm bmhhmwj nezue ywm mzhemw dxiabmc xl kw wmlbyumc aq khemw bmhhmw sxiamwj kw jqiakbj kfhms eknmomw hem ikwm fyizbzyw nkwc ukcm zj xjmc hk imys mzhemw y ukcm kw uzlemw"
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
        #print(key)
        cleanUp(key)

    for letter in key:
        print(letter + ": " + str(key[letter]))


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

main()
