import nltk

# Define the ambiguous grammar
groucho_grammar = nltk.CFG.fromstring("""
S  -> NP VP
NP -> Det N | N | NP PP
VP -> V NP | V VP | V NP PP
PP -> P NP
Det -> 'The' | 'a'
N -> 'can' | 'water'
V -> 'can' | 'hold'
P -> 'of'
""")

# Input sentence
sent = ['The', 'can', 'can', 'hold', 'a', 'can', 'of', 'water']

# Initialize parser
parser = nltk.ChartParser(groucho_grammar)

# Collect and print parse trees
parse_trees = list(parser.parse(sent))
for tree in parse_trees:
    print(tree)  # Print tree in text format
    tree.draw()  # Display graphical tree visualization

# Check for ambiguity
if len(parse_trees) > 1:
    print("Ambiguous grammar")
else:
    print("Unambiguous grammar")
