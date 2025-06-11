import spacy

# Load spaCy's English NLP model
nlp = spacy.load("en_core_web_sm")

# Function to build a full syntactic tree with all modifiers
def build_tree(token):
    children = list(token.children)

    # Handle determiners, adjectives, compounds, possessives for nouns
    if token.pos_ == "NOUN" or token.dep_ in ("nsubj", "dobj", "pobj", "attr"):
        dets = [build_tree(child) for child in children if child.dep_ == "det"]
        poss = [build_tree(child) for child in children if child.dep_ == "poss"]
        amods = [build_tree(child) for child in children if child.dep_ == "amod"]
        compounds = [build_tree(child) for child in children if child.dep_ == "compound"]
        full_np = dets + poss + compounds + amods + [f"(N {token.text})"]
        return f"(NP {' '.join(full_np)})"

    # Handle adjectives
    elif token.pos_ == "ADJ":
        return f"(ADJP (Adj {token.text}))"

    # Handle adverbs
    elif token.pos_ == "ADV":
        return f"(AdvP (Adv {token.text}))"

    # Handle verbs with auxiliaries, negation, adverb modifiers, and objects
    elif token.dep_ in ("ROOT", "aux", "cop", "conj"):
        aux = [build_tree(child) for child in children if child.dep_ == "aux"]
        neg = [build_tree(child) for child in children if child.dep_ == "neg"]
        advmod = [build_tree(child) for child in children if child.dep_ == "advmod"]
        objs = [build_tree(child) for child in children if child.dep_ in ("dobj", "attr", "prep", "pobj", "nsubj", "ccomp")]
        lefts = list(token.lefts)
        rights = list(token.rights)
        others = [build_tree(child) for child in children if child not in lefts + rights]

        return f"(VP {' '.join(aux + neg)} (V {token.text}) {' '.join(advmod + objs + others)})"

    # Handle prepositional phrases
    elif token.dep_ == "prep":
        pobj = [build_tree(child) for child in children if child.dep_ == "pobj"]
        return f"(PP (P {token.text}) {' '.join(pobj)})"

    # Handle negation
    elif token.dep_ == "neg":
        return f"(Neg {token.text})"

    # Handle conjunction
    elif token.dep_ == "cc":
        return f"(CC {token.text})"

    # Default case (fallback)
    elif children:
        return f"({token.text} {' '.join(build_tree(child) for child in children)})"
    else:
        return f"({token.text})"

# Input sentence
sentence = input("Enter a sentence to parse: ")

# Process the sentence
doc = nlp(sentence)

# Find the root of the sentence
root = next((token for token in doc if token.dep_ == "ROOT"), None)

# Build and print the parse tree
if root:
    parse_tree = f"(S {build_tree(root)})"
    print("\nTop-down parsing output:")
    print(parse_tree)
else:
    print("No ROOT verb found. Please enter a complete sentence.")