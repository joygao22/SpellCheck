# SpellCheck
This repository contains a Python script for a spell-checking tool that utilizes a BK-tree data structure. The spell checker can be used through the command line, allowing users to input text and specify the number of suggestions for corrections. The BK-tree implementation is based on the Bloom_filter module.

**Features:**
**Command-line interface:** Enables users to input text and specify the number of suggestions for corrections directly from the command line.
**BK-tree:** Efficiently searches for similar words based on Levenshtein distance.
**Integration with Levenshtein distance:** Utilizes Levenshtein distance for similarity calculation.
**Automatic population of BK-tree:** Populates the BK-tree with a comprehensive English dictionary before spell-checking.

**Usage:**
1. Clone the repository to your local machine.
2. Install the required dependencies, including NLTK (Natural Language Toolkit).
3. Run the SpellCheck.py script from the command line and follow the instructions to input text and specify the number of suggestions for corrections.
