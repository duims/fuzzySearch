import json
import itertools


def lev(w1, w2):
    # Calculates the distance between 2 words
    if w1 == w2:
        return 0

    # Hamming
    diff = 0

    if len(w1) == len(w2):
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
        return diff

    if len(w1) == 0:
        return len(w2)
    if len(w2) == 0:
        return len(w1)

    mat = [[] for i in range(len(w2) + 1)]
    for i in range(len(w2) + 1):
        for j in range(len(w1) + 1):
            mat[i].append(0)

    # set up matrix boundaries
    for i in range(1, len(w2) + 1):
        mat[i][0] = i
    for j in range(1, len(w1) + 1):
        mat[0][j] = j

    for j in range(1, len(w1) + 1):
        for i in range(1, len(w2) + 1):
            cost = 1
            if w1[j-1] == w2[i-1]:
                cost = 0

            mat[i][j] = min(mat[i - 1][j] + 1,
                            mat[i][j - 1] + 1,
                            mat[i - 1][j - 1] + cost)

    return mat[i][j]


def leven(w1, w2, errMax):
    # calculates if 2 words are within the error bound wrt distance
    # Calls lev(w1, w2)
    # w2 smaller pls:

    # if the length difference is too big for our search params, we aren't
    # even bothering to calculate
    if abs(len(w1) - len(w2)) - errMax > 0:
        return False

    errCount = lev(w1, w2)

    if errCount <= errMax:
        return True
    else:
        return False


def main():
    # index=index_read_file("text/cleanTestData.txt")
    # dump_index(index,"text/indexDump.txt")
    # index = read_saved_index("text/indexDump.txt")
    pass


def search(w1, maxDiff):
    # Returns w1 list of the words that match the upper bound.
    pass


def read_saved_index(fileName):
    with open(fileName, 'r') as file:
        index = json.load(file)
    return index


def dump_index(index, fileName):
    with open(fileName, "w") as file:
        json.dump(index, file)
    return


def index_read_file(fileName):
    # create w1 word index: {"cat":[1, 6, 100], 'mat':[2, 105, 238]}
    lineCount = 1
    index = {}
    with open(fileName, "r") as data:
        for line in data:
            words = line.split()
            for x in words:
                if x not in index:
                    index[x] = [lineCount]
                else:
                    index[x].append(lineCount)

            lineCount += 1
    return index


def write_stats(word, maxDiff, numMatches):
    # adds data point to end of file of word, errMax, number of levenshtein
    # matches.
    with open("searchRecord.txt", "w1") as statsFile:
        statsFile.write("{0},{1},{2}".format(word, maxDiff, numMatches))
    return

main()
