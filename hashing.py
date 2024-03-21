
def asciiHash(letters, tableSize):
    sum = 0
    for i in letters:
        sum += ord(i)
    sum = sum % int(tableSize)
    return str(sum)

def jenkinsHash(letters, tableSize):
    h=0
    for i in letters:
        h += ord(i)
        h += h << 10
        h ^= h >> 6
    h += h << 3
    h ^= h >> 11
    h += h << 15
    h = h % int(tableSize)
    return str(h)

def divisionHash(letters, seed, tableSize):
    sum = 0
    prime = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    lettersNum = len(letters)
    for i in range(lettersNum):
        temp = int(prime[int(seed)]) ** int(i)
        sum += int(ord(letters[i])) * temp
    sum = sum % int(tableSize)
    return str(sum)

def fnv1aHash(letters, seed, tableSize):
    offsetBasis = 0x811c9dc5
    prime = [16777619, 16777633, 16777639, 16777643, 16777669, 16777679, 16777681, 16777699, 16777711, 16777721]
    primeSeed = prime[int(seed)]
    h = offsetBasis
    key = letters.encode('utf-8')

    lettersNum = len(letters)
    for i in key:
        h ^= i
        h = h * primeSeed
        h &= 0xFFFFFFFF
    h = h % int(tableSize)
    return str(h)

def solve(input):
    inputSplit = input.split(",")
    if inputSplit[0] == "ascii_sum":
        stringInput = inputSplit[2].strip()
        letters = []
        for char in stringInput:
            letters.append(char)
        tableSize = inputSplit[1]
        return str(asciiHash(letters,tableSize))

    if inputSplit[0] == "jenkins":
        stringInput = inputSplit[2].strip()
        letters = []
        for char in stringInput:
            letters.append(char)
        tableSize = inputSplit[1]
        return str(jenkinsHash(letters, tableSize))

    if inputSplit[0] == "division":
        stringInput = inputSplit[3].strip()
        letters = []
        for char in stringInput:
            letters.append(char)
        seed = inputSplit[2]
        tableSize = inputSplit[1]
        return str(divisionHash(letters,seed, tableSize))

    if inputSplit[0] == "fnv1a":
        letters = inputSplit[3].strip()
        # letters = []
        # for char in stringInput:
        #     letters.append(char)
        seed = inputSplit[2]
        tableSize = inputSplit[1]
        return str(fnv1aHash(letters, seed, tableSize))
