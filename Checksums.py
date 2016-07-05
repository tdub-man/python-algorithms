# Takes a file with a list of checksums
# (one on each line) and compeares each
# to the checksums of the corresponding
# files in the folder, reporting result

from subprocess import check_output as output

def removeNewLines(arr):
    return list(map((lambda s: s[:-1]),arr))
def printEach(arr):
    for a in arr:
        print(a)
def verboseOutput(f):
    ret = output(["md5sum", f])
    print(ret[:-1].decode("utf-8"))
    return ret

checksums = open("checksums.txt")
sumsList = checksums.readlines()[:-1]
checksums.close()

sumsList = removeNewLines(sumsList)

# printEach(sumsList)

fileNames = list(map((lambda s: s.split(' ')[2]),sumsList))

# printEach(fileNames)

checkResults = [ output(["md5sum", f]) for f in fileNames ]
checkResults = removeNewLines(checkResults)
checkResults = list(map((lambda r: r.decode("utf-8")),checkResults))

# printEach(checkResults)

sumMatches = [ a == b for a,b in zip(sumsList,checkResults) ]

if all(sumMatches):
    print("MD5's all match")
else:
    print("One or more MD5's do not match")

# printEach(sumMatches)
