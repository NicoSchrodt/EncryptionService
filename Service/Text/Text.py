from Service.Text.EligibleCharacters import EligibleCharacters


class Text:
    def __init__(self):
        self.character_list = []
        self.cipher_character_list = []
        self.eligible_characters = EligibleCharacters()

    def fill_character_list(self, characters):
        temp = characters.upper()
        for i in range(len(temp)):
            self.character_list.append(temp[i])
        # stuff that fills the character_list
        pass

    def output_file(self, path):
        # outputs current character_list in chosen path
        pass

    def clear_plaintext(self):
        self.character_list = []

    def clear_ciphertext(self):
        self.cipher_character_list = []

    def set_eligible_characters(self, def_list):
        self.eligible_characters.insert_into_character_list(def_list)

    def get_eligible_characters(self):
        return self.eligible_characters.character_list
