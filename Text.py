class Text:
    def __init__(self):
        self.character_list = []
        self.cipher_character_list = []

    def fill_list(self, characters):
        for i in range(len(characters)):
            self.character_list.append(characters[i])
        # stuff that fills the character_list
        pass

    def output_file(self, path):
        # outputs current character_list in chosen path
        pass

    def encrypt(self, key):
        """Encrypt Text and return an encrypted text object"""
        pass

    def decrypt(self, key):
        """Decrypt Text and return an decrypted text object"""
        pass

    def clear_plaintext(self):
        self.character_list = []

    def clear_ciphertext(self):
        self.cipher_character_list = []