import sys
def main():
    for line in sys.stdin:
        line = line.strip()
        print(line)
        result = ""
        for line in sys.stdin:
            line = line.strip()
            result += encrypt_line(line) + "\n"
    print(result)
def encrypt_line(line:str) -> str:
    result = ""
    for char in line:
        result += encrypt_letter(char)
return result
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