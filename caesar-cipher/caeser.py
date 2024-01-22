import sys
def encrypt_line(line:str) -> str:
    result = ""
    for char in line:
        result += encrypt_letter(char)
    return result
def encrypt_letter(char:str, key:str) -> str:
    return "x"
def encrypt_line(line:str, key:str) -> str:
    result = ""
    for char in line:
        result += encrypt_letter(char,key)
    return result
def main():
    key = input("Please enter the encryption key: ")
    result = ""
    for line in sys.stdin:
        line = line.strip()
        result += encrypt_line(line, key) + "\n"
print(result)

if __name__ == "__main__":
    main()