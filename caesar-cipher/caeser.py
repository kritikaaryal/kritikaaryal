import sys

OUT_OF_BOUNDS = 127
FIRST_VISIBLE = 32
RANGE = OUT_OF_BOUNDS - FIRST_VISIBLE

def encrypt_letter(char: str, key: str) -> str:
    return chr((ord(char) - FIRST_VISIBLE + key) % RANGE + FIRST_VISIBLE)

def encrypt_line(line: str, key: str, mode="encrypt") -> str:
    sign = 1
    if mode.lower() == "decrypt" or mode.lower() == "d":
        sign = -1
    shift = (ord(key[0]) - 32) * sign
    result = ""
    for char in line:
        result += encrypt_letter(char, shift)
    return result

def main_menu() -> str:
    print("[1] Enter Encryption Key")
    print("[2] Encrypt a Message")
    print("[3] Decrypt a Message")
    print("[0] Exit Program")
    return input("Please select an option: ").strip()

def encrypt_message(key: str, mode="encrypt") -> None:
    result = ""
    for line in sys.stdin:
        line = line.strip()
        result += encrypt_line(line, key, mode) + "\n"
    print(result)

def main():
    key = ""  
    command = main_menu()
    while command != "0":  
        if command == "1":  
            key = input("Please enter the encryption key: ")
        elif command == "2" or command == "3":  
            if not key:
                print("Please enter the encryption key first.")
            else:
                encrypt_message(key, mode="decrypt" if command == "3" else "encrypt")
        else:
            print("Invalid entry. Please select a valid option.")
        command = main_menu()
    print("Goodbye.")

if __name__ == "__main__":
    main()