import nltk.corpus
import sys
import Levenshtein
import Bloom_filter
import identifyWord


tree = Bloom_filter.BKTree(Levenshtein.distance)

def populate():
    global tree
    wn = list(nltk.corpus.wordnet.words())
    wordList = list(nltk.corpus.words.words()) + list(nltk.corpus.brown.words()) + wn


    for word in wordList:
        tree.insert(word)
    tree.populatedFlag = True

def solve(input):
    global tree
    if not tree.is_populated():
        populate()
    splitInput = input.split("")
    while True:
        try:
            k = int(input("How many closest words do you want to output for each misspelled word? "))
            break  # Exit the loop if input is successfully converted to an integer
        except ValueError:
            print("Please enter a valid integer.")
    with open("SpellCheck.txt", "w") as file:
        for i in splitInput:
            closest_words = tree.find_k_closest(i, k)
            file.write(f"Closest words for {i}: {closest_words}\n")

def main():
    # Taking command-line arguments
    arguments = sys.argv[1:]
    if len(arguments) < 2:
        print("Usage: python script.py <input_text> <k>")
        sys.exit(1)
    input_text = arguments[0]
    k = int(arguments[1])
    text = identifyWord.findWords(input_text)
    solve(text, k)

if __name__ == "__main__":
    main()
