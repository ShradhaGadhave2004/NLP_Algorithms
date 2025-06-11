import nltk
from nltk.corpus import wordnet

# Download required WordNet data
nltk.download('wordnet')
nltk.download('omw-1.4')

def find_synonyms_antonyms():
    """Find and display synonyms and antonyms of a given word."""
    word = input("\nEnter a word to find synonyms and antonyms: ").strip()
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())  # Add synonyms
            if l.antonyms():  # Check and add antonyms
                antonyms.append(l.antonyms()[0].name())

    print("\nSynonyms:", set(synonyms) if synonyms else "No synonyms found.")
    print("Antonyms:", set(antonyms) if antonyms else "No antonyms found.")

def compare_word_similarity():
    """Compare the similarity between two words using Wu-Palmer Similarity."""
    word1 = input("\nEnter the first word: ").strip()
    word2 = input("Enter the second word: ").strip()

    synsets1 = wordnet.synsets(word1)
    synsets2 = wordnet.synsets(word2)

    if not synsets1 or not synsets2:
        print("\nOne or both words not found in WordNet.")
        return

    # Select the first synset (most common meaning)
    similarity = synsets1[0].wup_similarity(synsets2[0])

    print(f"\nWu-Palmer Similarity between '{word1}' and '{word2}': {similarity:.2f}" if similarity else "No similarity found.")

def get_definitions_and_examples():
    """Retrieve and display definitions and examples of a given word."""
    word = input("\nEnter a word to get definitions and examples: ").strip()
    synsets = wordnet.synsets(word)

    if not synsets:
        print("No definitions found for this word.")
        return

    print(f"\nDefinitions and examples for '{word}':")
    for i, syn in enumerate(synsets):
        print(f"{i+1}. {syn.definition()}")
        examples = syn.examples()
        if examples:
            print("   Examples:", "; ".join(examples))

def main():
    """Menu-driven program for WordNet operations."""
    while True:
        print("\nMenu:")
        print("1. Find Synonyms & Antonyms")
        print("2. Compare Word Similarity")
        print("3. Get Definitions & Examples")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            find_synonyms_antonyms()
        elif choice == "2":
            compare_word_similarity()
        elif choice == "3":
            get_definitions_and_examples()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

# Run the program
main()

