import random
import sys

def expand(grammar: dict) -> str:

    todo = todo + random.choice(grammar["<start>"])
    result = " "

    while todo:
        production = todo.pop(0)

        if production in grammar:
          
            replacement = random.choice(grammar[production])
            todo = todo + random.choice(grammar["<start>"])
        else:
            result = result + production
         
    return result.strip()

def poem() -> dict:
       start = []
       obj = []
       verb = []
       adverb = []
       nonterminals = {"<start>": start, "<object>":obj, "<verb>":verb, "<adverb>": adverb}
       start.append(["The","<object>", "<verb>", "tonight"])
       obj.append(["waves"])
       obj.append(["big","yellow","flowers"])
       obj.append(["slugs"])
       verb.append(["jumps"])
       verb.append(["runs"])
       verb.append(["screams"])
       adverb.append(["quietly"])
       adverb.append(["rapidly"])
       adverb.append(["smoothly"])

todo = ["The", "<object>", "<verb>", "tonight"]
result = ""

todo = ["<object>", "<verb>", "tonight"]
result = "The "
todo = ["big", "yellow", "flowers", "<verb>", "tonight"]
result = "The "
todo = ["<verb>", "tonight"]
result = "The big yellow flowers "

todo = ["sigh", "<adverb>", "tonight"]
result = "The big yellow flowers "

todo = ["<adverb>", "tonight"]
result = "The big yellow flowers sigh "

todo = ["warily", "tonight"]
result = "The big yellow flowers sigh "

todo = ["tonight"]
result = "The big yellow flowers sigh warily "

todo = []
result = "The big yellow flowers sigh warily tonight"
            
   

def parse_grammar(text: str) -> dict:
    nonterminals = {}
    text = text.strip()
    text= text.replace("\n", "")
    begin = 0
    end = 0
    while text.find("<", end) !=-1:
        begin = text.find("<",end)
        end = text.find(">", begin)
        key = text[begin:end+1]
        nonterminals[key]=[].strip()
        begin = text.find("=",end)
        end = text.find(";",begin)
        productions = text[begin:end]
    return nonterminals

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nonterminals = parse_grammar(file.read())
    else:
        nonterminals = poem()
    print(expand(nonterminals))
#string operations
    #s = "foobar"
    #print(s[1]) -> '0'
    #substring = s[1:3] -> "00"
    
def main():
    print(expand(poem()))
    print(poem())
    

