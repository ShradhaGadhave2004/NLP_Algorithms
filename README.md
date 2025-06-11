# NLP Algorithms

This repository contains Python implementations of classic Natural Language Processing (NLP) algorithms using libraries like **spaCy**, **NLTK**, and more. Each file demonstrates a specific NLP concept such as parsing, dependency trees, syntactic trees, etc.

---

## 🎯 Features

- Demonstartes simple NLP concepts.
- Have visual display of algorithm outputs for better understanding.
- Covers the following algorithms and concepts from NLP:
  - Simple Parsing of sentence.
  - Syntactic Parsing : Top-down Chart, Bottom-up Chart, Shift-Reduce and Recursive-Descent
  - Wordnet Basic Usage
  - Viterbi Algorithm

---

## 🛠️ Tech Stack

- **Python 3**

---

## 📦 Requirements

- Python 3.6 or higher
- Required Python packages:
  ```bash
  pip install spacy nltk
  python -m spacy download en_core_web_sm

---

## 🚀 Getting Started

1. Clone the Repository
 ```bash
 git clone https://github.com/yourusername/NLP_Algorithms.git
 ```
2. Run the script:
```bash
python name_of_python_file_from_folder.py
```
Note: Replace 'name_of_python_file_from_folder' with the algorithm file you want to run from the folder.

## 🧠 NLP Concepts Covered
This repository includes implementations and demonstrations of the following Natural Language Processing (NLP) algorithms and techniques:

### 🔍 Simple Parsing of Sentences
Demonstrates how to tokenize and syntactically analyze sentences using tools like spaCy and NLTK. Useful for understanding sentence structure and part-of-speech tagging.

### 🌳 Syntactic Parsing Techniques
Implements multiple parsing strategies to understand grammar and structure of sentences based on a Context-Free Grammar (CFG):

**Top-Down Chart Parser**: Starts from the start symbol and tries to rewrite it to the input sentence using chart parsing.

**Bottom-Up Chart Parser**: Builds parse trees from the input tokens upward toward the start symbol using dynamic programming.

**Shift-Reduce Parser**: A stack-based parsing method that uses shift and reduce operations to build parse trees.

**Recursive-Descent Parser**: A top-down parser built using mutually recursive functions that try to match grammar rules to the input tokens.

### 🧾 WordNet Basic Usage
Shows how to use WordNet, a lexical database of English, via NLTK for:

- Finding synonyms, antonyms

- Getting definitions and examples

- Understanding semantic similarity

### 🔁 Viterbi Algorithm
Implements the Viterbi algorithm for part-of-speech tagging using a Hidden Markov Model (HMM). It finds the most probable sequence of tags for a given sentence based on training data.

## 👩‍💻 Author
Shradha Gadhave
