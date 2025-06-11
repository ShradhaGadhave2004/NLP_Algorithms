import sys
from nltk.parse import ShiftReduceParser, RecursiveDescentParser, BottomUpChartParser, TopDownChartParser
from nltk import CFG

# Define the grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'ball'
    V -> 'chased' | 'barked' | 'rolled'
""")

# Available sentences
sentences = {
    '1': "the cat chased the dog",
    '2': "the dog barked",
    '3': "the ball rolled"
}

def parse_sentence(parser, sentence, parser_name, is_chart_parser=False):
    words = sentence.split()
    print(f"\n{'='*40}\n{parser_name} for sentence: '{sentence}'\n{'='*40}")

    # If using a chart parser, trace is already set, so parsing will show the chart
    if is_chart_parser:
        trees = list(parser.parse(words))  # This will display the chart first
    else:
        trees = list(parser.parse(words))  # Convert to list to prevent exhaustion

    if trees:
        print("\nParse Tree(s):")
        for tree in trees:
            tree.pretty_print()  # Print parse tree in the console
    else:
        print("Invalid. No Output.")

    print("\nReturning to the menu...\n")  # Message before showing the menu again
        
def main():
    while True:
        print("\nChoose a sentence:")
        for key, sentence in sentences.items():
            print(f"{key}. {sentence}")
        print("4. Exit")

        sentence_choice = input("Enter your choice (1-4): ")
        if sentence_choice == '4':
            print("Exiting program...")
            break
        elif sentence_choice not in sentences:
            print("Invalid choice. Please select again.")
            continue

        sentence = sentences[sentence_choice]

        print("\nChoose a parsing method:")
        print("1. Bottom-Up Shift-Reduce Parsing")
        print("2. Top-Down Recursive Descent Parsing")
        print("3. Bottom-Up Chart Parsing")
        print("4. Top-Down Chart Parsing")

        parser_choice = input("Enter your choice (1-4): ")

        if parser_choice == '1':
            parser = ShiftReduceParser(grammar)
            parse_sentence(parser, sentence, "Bottom-Up Shift-Reduce Parsing")
        elif parser_choice == '2':
            sys.setrecursionlimit(1500)  # Avoid recursion limit errors
            parser = RecursiveDescentParser(grammar)
            parse_sentence(parser, sentence, "Top-Down Recursive Descent Parsing")
        elif parser_choice == '3':
            parser = BottomUpChartParser(grammar, trace=2)  # Enable trace for chart display
            parse_sentence(parser, sentence, "Bottom-Up Chart Parsing", is_chart_parser=True)
        elif parser_choice == '4':
            parser = TopDownChartParser(grammar, trace=1)  # Enable trace for chart display
            parse_sentence(parser, sentence, "Top-Down Chart Parsing", is_chart_parser=True)
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
