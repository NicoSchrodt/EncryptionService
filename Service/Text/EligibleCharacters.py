import string

special_characters = [".", ",", ";", "?", "!", "&", "%", "(", ")", "=", "+", "-", "?", "\"", "'", "@"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class EligibleCharacters:
    def __init__(self):
        self.character_list = []

    def insert_predefined_into_character_list(self, chars):
        if "std" in chars:
            for i in range(len(string.ascii_uppercase)):
                self.character_list.append(string.ascii_uppercase[i])
        if "std_low" in chars:
            for i in range(len(string.ascii_lowercase)):
                self.character_list.append(string.ascii_lowercase[i])
        if "sc" in chars:
            self.character_list.append(special_characters)
        if "nmb" in chars:
            self.character_list.append(numbers)

    def get_character_list(self):
        return self.character_list

    # Developer function, generally don't use
    def set_character_list(self, char_list):
        self.character_list = char_list

    def add_to_character_list(self, char_list):
        for i in char_list:
            self.character_list.append(i)
