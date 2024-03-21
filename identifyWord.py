import Bloom_filter
import nltk.corpus

bloom = Bloom_filter.BloomFilter(18000000, 22)
def populate():
    wn = []
    for word in nltk.corpus.wordnet.words():
        wn.append(word)
    wordList = []
    for i in nltk.corpus.words.words():
        wordList.append(i)
    for j in nltk.corpus.brown.words():
        wordList.append(j)
    for k in wn:
        wordList.append(k)

    for i in wordList:
        sum1 = 0
        sum1 += bloom.addAscii(i, 18000000)

        sum1 += bloom.addJenkins(i, 18000000)

        for j in range(10):
            sum1 += bloom.addDivision(i, j, 18000000)

        for k in range(10):
            sum1 += bloom.addFnv1a(i, k, 18000000)
    bloom.populated = True

def findWords(input):

    global bloom  # Access the global Bloom filter instance

    # Check if the Bloom filter is populated
    if not bloom.is_populated():
        populate()
    punctuation = '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~'

    # Define characters to keep
    keep_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' -")

    # Initialize an empty string to store the cleaned text
    cleanedText = ''

    # Iterate over each character in the input text
    for char in input:
        # Check if the character is in the set of characters to keep
        if char in keep_characters:
            # Add the character to the cleaned text
            cleanedText += char
    splitWords = cleanedText.split()
    falseItems = []
    for i in splitWords:
        if bloom.query(i,18000000) == False:
            falseItems.append(i)

    return str(falseItems)