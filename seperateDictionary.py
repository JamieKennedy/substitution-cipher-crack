def main():
    wordsSep = {}
    with open("dictionary.txt") as dictionary:
        words = dictionary.readlines()

    for word in words:
        word = word.replace("\n", "")
        if len(word) not in wordsSep:
            wordsSep[len(word)] = [word]
        else:
            wordsSep[len(word)].append(word)

    for key in wordsSep:
        words = wordsSep[key]
        data = "".join(word + "\n" for word in words)
        fileName = "dicts/dictionaryLen" + str(key) + ".txt"
        writeFile(fileName, data)


def writeFile(fileName, data):
    file = open(fileName, "w")
    file.write(data)
    file.close()


main()
