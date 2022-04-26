from Service.Analysis.Kasiski.Kasiski import Kasiski
from Service.Analysis.Helpers.const import (SEQ_LEN, MAX_KEY_LEN)


def guessKey(ciphertext):
    key_len = 0
    KT = Kasiski()
    key_len = KT.find_key_length(ciphertext=ciphertext, seq_len=SEQ_LEN, max_key_len=MAX_KEY_LEN)
    return key_len
