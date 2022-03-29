import abc


class EncrypterInterface(metaclass=abc.ABCMeta):
    def __init__(self, reference):
        self.text = reference

    @abc.abstractmethod
    def encrypt(self, key):
        # Encrypt the character list in text-object
        raise NotImplementedError

    @abc.abstractmethod
    def decrypt(self, key):
        # Decrypt the character list in text-object
        raise NotImplementedError
