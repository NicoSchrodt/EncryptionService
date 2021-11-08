from Text import Text
from VigenereEncryption import encryptVig


class VigenereText(Text):
    def __init__(self):
        super().__init__()
        self.set_eligible_characters("std")

    def encrypt(self, key):
        """Encrypt Text and return an encrypted text object"""
        encryptVig(self, key)
        pass

    def decrypt(self, key):
        """Decrypt Text and return an decrypted text object"""
        pass
