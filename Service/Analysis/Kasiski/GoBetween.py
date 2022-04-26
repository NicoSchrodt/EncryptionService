from Service.Analysis.Kasiski.Kasiski import find_key_length
from Service.Analysis.Helpers.const import (SEQ_LEN, MAX_KEY_LEN)


def guessKey(ciphertext):
    key_len = 0
    key_len = find_key_length(cyphertext=ciphertext, seq_len=SEQ_LEN, max_key_len=MAX_KEY_LEN)
    return key_len
