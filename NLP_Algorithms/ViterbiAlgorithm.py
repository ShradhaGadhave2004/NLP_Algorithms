import nltk
import time
from nltk.parse import ViterbiParser
from nltk import PCFG

# Define sentence
sent = "I saw the man with my telescope"
tokens = sent.split()  # Tokenizing the sentence

# Define PCFG grammar
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    V -> 'saw' [1.0]
    NP -> DT N [0.5] | PRP [0.25] | PRP_POS N [0.25]
    DT -> 'the' [1.0]
    N -> 'man' [0.5] | 'telescope' [0.5]
    P -> 'with' [1.0]
    PRP -> 'I' [1.0] 
    PRP_POS -> 'my' [1.0]
""")

# Initialize parser
parser = ViterbiParser(grammar)

# Measure parsing time
start_time = time.time()
parses = list(parser.parse_all(tokens))
elapsed_time = time.time() - start_time  # Calculate elapsed time

num_parses = len(parses)

# Print parsing details
print("\nSentence: ", sent)
print("Time taken for parsing: %.6f seconds" % elapsed_time)
print("Number of parses found:", num_parses)
print("\nParse Trees:\n")

# Display parse trees
for i, parse in enumerate(parses, start=1):
    print(f"Parse {i}:")
    print(parse)
    print("\n")

# Draw the first parse tree if available
if parses:
    parses[0].draw()
