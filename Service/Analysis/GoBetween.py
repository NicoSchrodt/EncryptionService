import Kasiski
from Helpers.const import (SEQ_LEN, MAX_KEY_LEN)


def guessKey(file, method):
    with open(file) as f:
        cyphertext = f.readlines()
        key_len = 0
        if method == 'kasiski':
            print('Applying kasiski examination\n')
            key_len = Kasiski.find_key_length(cyphertext=cyphertext[0], seq_len=SEQ_LEN, max_key_len=MAX_KEY_LEN)
            print("Guessed Key length: " + str(key_len))


guessKey('input.txt', 'kasiski')
