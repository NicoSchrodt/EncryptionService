import string

special_characters = [".", ",", ";", "?", "!", "&", "%", "(", ")", "=", "+", "-", "?", "\"", "'", "@"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class EligibleCharacters:
    def __init__(self):
        self.character_list = []

    def insert_into_character_list(self, chars):
        if "std" in chars:
            temp = string.ascii_uppercase
            for i in range(len(temp)):
                self.character_list.append(temp[i])
        if "sc" in chars:
            self.character_list.append(special_characters)
        if "nmb" in chars:
            self.character_list.append(numbers)

