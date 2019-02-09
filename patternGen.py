import os
import json


def main(dirName):
    files = getFiles(dirName)
    for file in files:
        words = readFile("dicts/" + file)
        patterns = {}

        for word in words:
            pattern = getPattern(word)
            if pattern not in patterns:
                patterns[pattern] = [word]
            else:
                patterns[pattern].append(word)

        writeJson(file, patterns)


def writeJson(fileName, data):
    file = open("jsonDicts/" + fileName.split(".")[0] + ".json", "w")
    file.write(json.dumps(data))
    file.close()


def readFile(fileName):
    with open(fileName) as file:
        lines = [line.rstrip() for line in file]

    return lines


def getFiles(directory):
    directory = os.fsencode(directory)
    files = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            files.append(filename)

    return files


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


main("dicts")
