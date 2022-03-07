from Service.Encryption.Encrypter import Encrypter


def encryptVig(reference, key):
    key_list = [char for char in key.upper()]
    key_len = len(key_list)
    key_counter = 0
    index_new = 0
    print(key_list)
    local_list = reference.character_list
    local_eligible_character_list = reference.get_eligible_characters()
    num_elg_chars = len(local_eligible_character_list)
    print(local_eligible_character_list)
    for i in range(len(local_list)):
        try:
            index_char = local_eligible_character_list.index(local_list[i])
            index_key = local_eligible_character_list.index(key_list[key_counter])
            index_new = index_char + index_key
            while index_new >= num_elg_chars:
                index_new -= num_elg_chars
            reference.cipher_character_list.append(local_eligible_character_list[index_new])
            key_counter += 1
            if key_counter >= key_len:
                key_counter = 0
        except ValueError:  # This means character is not eligible, skip character
            reference.cipher_character_list.append(local_list[i])
            print("Invalid character '" + local_list[i] + "' found, skipped. "
                                                          "Please add a character-set which contains character.")


class VigenereEncrypter(Encrypter):
    def __init__(self, _reference):
        super().__init__(reference=_reference)

    def encrypt(self, key):
        key_list = [char for char in key.upper()]
        key_len = len(key_list)
        key_counter = 0
        print(key_list)
        local_list = self.text.character_list
        local_eligible_character_list = self.text.get_eligible_characters()
        num_elg_chars = len(local_eligible_character_list)
        print(num_elg_chars)
        print(local_eligible_character_list)
        for i in range(len(local_list)):
            try:
                index_char = local_eligible_character_list.index(local_list[i])
                index_key = local_eligible_character_list.index(key_list[key_counter])
                index_new = index_char + index_key
                while index_new >= num_elg_chars:
                    index_new -= num_elg_chars
                self.text.cipher_character_list.append(local_eligible_character_list[index_new])
                key_counter += 1
                if key_counter >= key_len:
                    key_counter = 0
            except ValueError:  # This means character is not eligible, skip character
                self.text.cipher_character_list.append(local_list[i])
                print("Invalid character '" + local_list[i] + "' found, skipped. "
                                                              "Please add a character-set which contains character.")

    def decrypt(self):
        pass
