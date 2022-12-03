import string

ALPHABET = string.ascii_uppercase
ALPHABET_LENGTH = len(ALPHABET)
ALPHABET_LENGTH_NEGATIVE = - ALPHABET_LENGTH

def encrypt(plaintext, encryption_key):
    """Encrypt cipher text."""
    encrypted_letters = []
    for letter in plaintext:
        if letter not in ALPHABET:
            encrypted_letters.append(letter)
        elif letter in ALPHABET:
            plain_letter_index = ALPHABET.index(letter)
            encrypted_letter_index = plain_letter_index + encryption_key
            try:
                encrypted_letters.append(ALPHABET[encrypted_letter_index])
            except IndexError:
                index_difference = ALPHABET_LENGTH - plain_letter_index
                index_check = index_difference - encryption_key
                while ALPHABET_LENGTH <= index_check or index_check < 0:
                    if index_check < 0:
                        index_check = (index_check*-1)
                    if index_check >= ALPHABET_LENGTH:
                        index_check = index_check - ALPHABET_LENGTH
                    if index_check == ALPHABET_LENGTH:
                        index_check = 0
                encrypted_letters.append(ALPHABET[index_check])
    encrypted_message = ''.join(encrypted_letters)
    return encrypted_message

  
def decrypt(ciphertext, encryption_key):
    """Decrypt ciphertext."""
    decrypted_letters = []
    for letter in ciphertext:
        if letter not in ALPHABET:
            decrypted_letters.append(letter)
        elif letter in ALPHABET:
            plain_letter_index = ALPHABET.index(letter)
            decrypted_letter_index = plain_letter_index - encryption_key
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


def brute_force(ciphertext, possible_keys=ALPHABET_LENGTH):
  """Print possible plaintext for the provided ciphertext."""
  for possible_key in range(1, possible_keys):
    possible_text = decrypt(ciphertext, possible_key)
    print(f"Key: {possible_key} - Plain text: {possible_text}")


if __name__ == "__main__":

    mode = int(input("1 - Code:\n2 - Decode:\n3 - Brute Force:\n"))

    match mode:
        case 1:
            key = int(input("Key: 1- 25: "))
            secret_message = input("Encode:\n")
            print_secret_message = encrypt(secret_message, key)
            print(print_secret_message)
        case 2:
            key = int(input("Key: 1- 25: "))
            ciphertext_to_decipher = input("Decode:\n")
            deciphered_text = decrypt(ciphertext_to_decipher, key)
            print(deciphered_text)
        case 3:
            secret_message = input("Brute Force:\n")
            brute_force(secret_message)