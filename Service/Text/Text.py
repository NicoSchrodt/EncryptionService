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

    def fill_cipher_list(self, characters):
        temp = characters.upper()
        for i in range(len(temp)):
            self.cipher_character_list.append(temp[i])

    def get_plain_string(self):
        return_string = ""
        for i in range(len(self.character_list)):
            return_string = return_string + self.character_list[i]
        return return_string

    def get_cipher_string(self):
        return_string = ""
        for i in range(len(self.cipher_character_list)):
            return_string = return_string + self.cipher_character_list[i]
        return return_string

    def output_file(self, path):
        # outputs current character_list in chosen path
        pass

    def clear_plaintext(self):
        self.character_list = []

    def clear_ciphertext(self):
        self.cipher_character_list = []

    def set_eligible_characters_list(self, def_list):
        self.eligible_characters.insert_predefined_into_character_list(def_list)

    def get_eligible_characters(self):
        return self.eligible_characters.character_list

    def set_eligible_characters(self, charset):
        self.eligible_characters = charset
