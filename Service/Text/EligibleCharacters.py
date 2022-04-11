import string

special_characters = [".", ",", ";", ":", "?", "!", "&", "%", "(", ")", "=", "+", "-", "?", "\"", "'", "@"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class EligibleCharacters:
    def __init__(self):
        self.character_list = []
        self.predefined_inserted = []

    def insert_predefined_into_character_list(self, chars):
        if "std" in chars and "std" not in self.predefined_inserted:
            self.add_to_character_list(string.ascii_uppercase)
            self.predefined_inserted.append("std")
        if "std_low" in chars and "std_low" not in self.predefined_inserted:
            self.add_to_character_list(string.ascii_lowercase)
            self.predefined_inserted.append("std_low")
        if "sc" in chars and "sc" not in self.predefined_inserted:
            self.add_to_character_list(special_characters)
            self.predefined_inserted.append("sc")
        if "nmb" in chars and "nmb" not in self.predefined_inserted:
            self.add_to_character_list(numbers)
            self.predefined_inserted.append("nmb")

    def get_character_list(self):
        return self.character_list

    # Developer function, generally don't use
    def set_character_list(self, char_list):
        self.character_list = char_list
        self.predefined_inserted = []

    def add_to_character_list(self, char_list):
        for i in char_list:
            if i not in self.character_list:
                self.character_list.append(i)
