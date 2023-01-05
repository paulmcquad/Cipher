import string

def ceasar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shift_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shift_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

def ceasar_decrypt(text, shift, alphabets):
    """Decrypt text."""
    ALPHABET = string.ascii_letters
    ALPHABET_LENGTH = len(alphabets)
    ALPHABET_LENGTH_NEGATIVE = - ALPHABET_LENGTH

    decrypted_letters = []
    for letter in text:
        if letter not in ALPHABET:
            decrypted_letters.append(letter)
        elif letter in ALPHABET:
            plain_letter_index = ALPHABET.index(letter)
            decrypted_letter_index = plain_letter_index - shift
            if decrypted_letter_index >= 0:
                decrypted_letters.append(ALPHABET[decrypted_letter_index])
            else:
                try:
                    decrypted_letter_index += ALPHABET_LENGTH
                    decrypted_letters.append(ALPHABET[decrypted_letter_index])
                except IndexError:
                        while decrypted_letter_index <= ALPHABET_LENGTH_NEGATIVE:
                            decrypted_letter_index = decrypted_letter_index + ALPHABET_LENGTH
                        decrypted_letters.append(ALPHABET[decrypted_letter_index])
    decrypted_message = ''.join(decrypted_letters)
    return decrypted_message


if __name__ == "__main__":
#    print(ceasar(plain_text, 7, [string.ascii_lowercase,string.ascii_uppercase, string.punctuation]))
    mode = int(input("1 - Encode:\n2 - Decode:\n3 - Brute Force:\n"))

    match mode:
        case 1:
            key = int(input("Key: 1- 25: "))
            secret_message = input("Encode:\n")
            print(ceasar(secret_message, key, [string.ascii_letters, string.punctuation]))
        case 2:
            key = int(input("Key: 1- 25: "))
            ciphertext_to_decipher = input("Decode:\n")
            print(ceasar_decrypt(ciphertext_to_decipher, key, [string.ascii_lowercase,string.ascii_uppercase, string.punctuation]))
        case 3:
            secret_message = input("Brute Force:\n")
            for key in range(26):
                print("Key {0}:".format(key), ceasar(secret_message, key, [string.ascii_letters, string.punctuation]))