import spacy
from nltk.tree import Tree
import nltk

# Download punkt tokenizer if not already available
nltk.download('punkt', quiet=True)

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Function to convert spaCy parse into NLTK Tree format
def to_nltk_tree(token):
    # If token has children, make a tree node
    if list(token.children):
        return Tree(f"{token.text} ({token.dep_})", [to_nltk_tree(child) for child in token.children])
    else:
        # Leaf node
        return f"{token.text} ({token.dep_})"

# Take sentence input from user
sentence = input("Enter a sentence to display tree: ")
doc = nlp(sentence)

# Find the ROOT token and build tree
root = next((token for token in doc if token.dep_ == "ROOT"), None)

# Display tree if ROOT exists
if root:
    tree = to_nltk_tree(root)
    print("\nText-based Tree Structure:\n")
    tree.pretty_print()     # ASCII format
    tree.draw()             # Opens GUI window
else:
    print("No ROOT verb found. Please enter a complete sentence.")
