import random
import sys

def expand(grammar: dict) -> str:
    todo = random.choice(grammar["<start>"])
    result = ""

    while todo:
        production = todo.pop(0)

        if production in grammar:
            replacement = random.choice(grammar[production])
            todo = replacement + todo
        elif len(production)>0 and production[0].isalnum():
            result = result + " " + production  
        else:
            result = result + production

    return result.strip()

def poem() -> dict:
    start = []
    obj = []
    verb = []
    adverb = []
    nonterminals = {"<start>": start, "<object>": obj, "<verb>": verb, "<adverb>": adverb}
    start.append(["The", "<object>", "<verb>", "tonight"])
    return nonterminals

def parse_grammar(text: str) -> dict:
    nonterminals = {}
    text = text.strip()
    text = text.replace("\n", "")
    text = text.replace("\\", "\n")
    begin = 0
    end = 0
    while text.find("<", end) != -1:
        begin = text.find("<", end)
        end = text.find(">", begin)
        key = text[begin:end + 1]
        nonterminals[key] = []
        begin = text.find("=", end)
        end = text.find(";", begin)
        productions = text[begin + 1:end]
        productions = productions.split("|")
        for production in productions:
            production = production.strip()
            tokens = production.split(" ")
            nonterminals[key].append(tokens)
    return nonterminals

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nonterminals = parse_grammar(open(sys.argv[1]).read())
    else:
        nonterminals = poem()
    print(expand(nonterminals))

def main():
    print(expand(poem()))