from Service.Encryption.EncrypterInterface import EncrypterInterface


class CaesarEncrypter(EncrypterInterface):
    def __init__(self, _reference):
        super().__init__(reference=_reference)

    def encrypt(self, key):
        # ToDo
        pass

    def decrypt(self, key):
        # ToDo
        pass
