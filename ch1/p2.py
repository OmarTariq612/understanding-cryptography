from common import *

ciphertext = """xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpit
ghlxiwiwtxgqadds"""

# from this we knew that 't' is has the most frequency in the cipher text,
# therefore '15' is the shift key
# print(count_chars(ciphertext))

for char in ciphertext:
    if not char.isalpha():
        print(char, end="")
    else:
        print(chr(((ord(char) - ord("a") - 15) % 26) + ord("a")), end="")

print("\n========================")

plaintext = "if we all unite we will cause the rivers to stain the great waters with their blood"

print("with spaces:\n========================")
print(plaintext)
