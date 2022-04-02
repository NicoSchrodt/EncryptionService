import string
import unittest

from unittest.mock import Mock, create_autospec

from Service.Encryption.CaesarEncrypter import CaesarEncrypter
from Service.Encryption.VigenereEncrypter import VigenereEncrypter
from Service.Text.CaesarText import CaesarText
from Service.Text.VigenereText import VigenereText
from Service.Text.EligibleCharacters import EligibleCharacters


class VigenereEncrypterTest(unittest.TestCase):

    def setUp(self):
        # -------------------Mock
        self.mock = create_autospec(VigenereText)
        temp = string.ascii_uppercase
        character_list = []
        for i in range(len(temp)):
            character_list.append(temp[i])
        self.mock.get_eligible_characters.return_value = character_list

    def test_vigenere_encrypter_encrypt(self):
        # -------------------Parameters
        self.mock.character_list = ['A', 'B', 'C', 'D']
        self.mock.cipher_character_list = []
        key = 'AAAA'
        expected_answer = ['A', 'B', 'C', 'D']
        # -------------------Encrypt
        encrypter = VigenereEncrypter(self.mock)
        encrypter.encrypt(key)
        answer = self.mock.cipher_character_list

        self.assertEqual(expected_answer, answer)

    def test_vigenere_encrypter_decrypt(self):
        # -------------------Parameters
        self.mock.character_list = []
        self.mock.cipher_character_list = ['A', 'B', 'C', 'D']
        key = 'AAAA'
        expected_answer = ['A', 'B', 'C', 'D']
        # -------------------Encrypt
        encrypter = VigenereEncrypter(self.mock)
        encrypter.encrypt(key)
        answer = self.mock.cipher_character_list

        self.assertEqual(expected_answer, answer)


class CaesarEncrypterTest(unittest.TestCase):

    def setUp(self):
        # -------------------Mock
        self.mock = create_autospec(CaesarText)
        temp = string.ascii_uppercase
        character_list = []
        for i in range(len(temp)):
            character_list.append(temp[i])
        self.mock.get_eligible_characters.return_value = character_list

    def test_caesar_encrypter_encrypt(self):
        # -------------------Parameters
        self.mock.character_list = ['A', 'B', 'C', 'D']
        self.mock.cipher_character_list = []
        key = 'B'
        expected_answer = ['B', 'C', 'D', 'E']
        # -------------------Encrypt
        encrypter = CaesarEncrypter(self.mock)
        encrypter.encrypt(key)
        answer = self.mock.cipher_character_list

        self.assertEqual(expected_answer, answer)

    def test_caesar_encrypter_decrypt(self):
        # -------------------Parameters
        self.mock.character_list = []
        self.mock.cipher_character_list = ['B', 'C', 'D', 'E']
        key = 'B'
        expected_answer = ['A', 'B', 'C', 'D']
        # -------------------Encrypt
        encrypter = CaesarEncrypter(self.mock)
        encrypter.decrypt(key)
        answer = self.mock.character_list

        self.assertEqual(expected_answer, answer)


class CharsetTest(unittest.TestCase):

    def setUp(self):
        self.charset = EligibleCharacters()
        self.assertEqual(self.charset.get_character_list(), [])

    def test_set_character_list(self):
        self.charset.set_character_list(["a", "b", "c"])
        self.assertEqual(self.charset.get_character_list(), ["a", "b", "c"])

    def test_add_to_character_list(self):
        self.charset.character_list = ["a", "b", "c"]
        self.charset.add_to_character_list(["d"])
        self.assertEqual(self.charset.get_character_list(), ["a", "b", "c", "d"])


if __name__ == '__main__':
    unittest.main()
