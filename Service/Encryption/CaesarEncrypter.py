from Service.Encryption.EncrypterInterface import EncrypterInterface


def check_key_length(key, length):
    if len(key) == length:
        return True
    else:
        return False


class CaesarEncrypter(EncrypterInterface):
    def __init__(self, _reference):
        super().__init__(reference=_reference)
        self.key_length = 1

    def encrypt(self, key):
        if not check_key_length(key, self.key_length):
            print("Invalid Key length!")
            raise ValueError
        key = self.validateKey(key)
        local_list = self.text.character_list
        local_eligible_character_list = self.text.get_eligible_characters()
        num_elg_chars = len(local_eligible_character_list)
        for i in range(len(local_list)):
            index_key = local_eligible_character_list.index(key)
            try:
                index_char = local_eligible_character_list.index(local_list[i])
                index_new = index_char + index_key
                while index_new >= num_elg_chars:
                    index_new -= num_elg_chars
                self.text.cipher_character_list.append(local_eligible_character_list[index_new])
            except ValueError:
                self.text.cipher_character_list.append(local_list[i])
                if local_list[i] != " ":
                    print("Invalid character '" + local_list[i] + "' found, skipped. Please add a character-set which "
                                                                  "contains character.")

    def decrypt(self, key):
        if not check_key_length(key, self.key_length):
            print("Invalid Key length!")
            raise ValueError
        key = self.validateKey(key)
        local_list = self.text.cipher_character_list
        local_eligible_character_list = self.text.get_eligible_characters()
        num_elg_chars = len(local_eligible_character_list)
        for i in range(len(local_list)):
            index_key = local_eligible_character_list.index(key)
            try:
                index_char = local_eligible_character_list.index(local_list[i])
                index_new = index_char - index_key
                while index_new < 0:
                    index_new += num_elg_chars
                self.text.character_list.append(local_eligible_character_list[index_new])
            except ValueError:
                self.text.character_list.append(local_list[i])
                if local_list[i] != " ":
                    print("Invalid character '" + local_list[i] + "' found, skipped. Please add a character-set which "
                                                                  "contains character.")
