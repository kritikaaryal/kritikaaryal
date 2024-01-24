import sys
OUT_OF_BOUNDS = 127
FIRST_VISIBLE = 32
RANGE = OUT_OF_BOUNDS - FIRST_VISIBLE # This evaluates to 95
if shifted_index >= OUT_OF_BOUNDS :
    shifted_index = shifted_index - OUT_OF_BOUNDS + FIRST_VISIBLE
def encrypt_letter(char:str, key:str) -> str:
# We will figure out how to do the encryption later.
# For now, we're just going to return the letter "x"
    return chr(ord(char) + key)

def encrypt_line(line:str, key:str, mode="encrypt") -> str:
    sign = 1
    if mode.lower() == "decrypt" or mode.lower() == "d":
        sign = -1
    shift = (ord(key[0]) - 32) * sign
    result = ""
    for char in line:
        result += encrypt_letter(char,shift)
    return result
def encrypt_message(key:str, mode="encrypt") -> None:
    result = ""
    for line in sys.stdin:
        line = line.strip()
        result += encrypt_line(line, key, mode) + "\n"
    print(result)
def main_menu() -> str:
    print("[1] Enter Encryption Key")
    print("[2] Encrypt a Message")
    print("[3] Decrypt a Message")
    print("[0] Exit Program")
# We call strip after calling input to get rid of any
# leading or trailing white space entered by the user
    return input("Please select an option: ").strip()
def main():
    command = main_menu()
    while command != "0": # Option to exit program
        if command == "1": # Option to change encryption key
            key = input("Please enter the encryption key: ")
         elif command == "2": # Option to encrypt a message
            encrypt_message(key)
        elif command == "3":
    # TODO: Replace "pass" below with the
    # code to decrypt a message
            pass
        else:
    print("Invalid entry. Please select a valid option.")
    command = main_menu()
    print("Goodbye.")
    

if __name__ == "__main__":
    main()

# import sys
# def encrypt_line(line:str) -> str:
#     result = ""
#         for char in line:
#     result += encrypt_letter(char,shift)
#         return result
#     return chr(ord(char) + key)
#     OUT_OF_BOUNDS = 127
#     FIRST_VISIBLE = 32
#     RANGE = OUT_OF_BOUNDS - FIRST_VISIBLE # This evaluates to 95
#     if shifted_index >= OUT_OF_BOUNDS :
#         shifted_index = shifted_index - OUT_OF_BOUNDS + FIRST_VISIBLE
#     return chr((ord(char) - FIRST_VISIBLE + KEY ) % RANGE + FIRST_VISIBLE)
# def encrypt_line(line:str, key:str, mode="encrypt") -> str:
#     sign = 1
#     if mode.lower() == "decrypt" or mode.lower() == "d":
#         sign = -1
#     shift = (ord(key[0]) - 32) * sign
#     result = ""
#     for char in line:
#     result += encrypt_letter(char,shift)
# return result
#         print(line)
#         result = ""
#         for line in sys.stdin:
#             line = line.strip()
#             result += encrypt_line(line) + "\n"
#     print(result)
# if __name__ == "__main__":
#     main()