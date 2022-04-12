import abc


class EncrypterInterface(metaclass=abc.ABCMeta):
    def __init__(self, reference):
        self.text = reference

    @abc.abstractmethod
    def encrypt(self, key):
        # Encrypt the character list in text-object
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    def decrypt(self, key):
        # Decrypt the character list in text-object
        raise NotImplementedError  # pragma: no cover

    def validateKey(self, key):
        Charset = self.text.get_eligible_characters()
        validKey = ""
        for i in key:
            if i in Charset:
                validKey = validKey + i
        return validKey
