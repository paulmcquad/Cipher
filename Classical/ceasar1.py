import string

def ceasar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shift_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shift_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)


if __name__ == "__main__":
#    print(ceasar(plain_text, 7, [string.ascii_lowercase,string.ascii_uppercase, string.punctuation]))
    mode = int(input("1 - Code:\n2 - Decode:\n3 - Brute Force:\n"))

    match mode:
        case 1:
            key = int(input("Key: 1- 25: "))
            secret_message = input("Encode:\n")
            print(ceasar(secret_message, key, [string.ascii_lowercase,string.ascii_uppercase, string.punctuation]))
        case 2:
            key = int(input("Key: 1- 25: "))
            ciphertext_to_decipher = input("Decode:\n")
            print(ceasar(ciphertext_to_decipher, key, [string.ascii_lowercase,string.ascii_uppercase, string.punctuation]))
        case 3:
            secret_message = input("Brute Force:\n")
            for key in range(26):
                print("Key {0}:".format(key), ceasar(secret_message, key, [string.ascii_lowercase,string.ascii_uppercase, string.punctuation]))