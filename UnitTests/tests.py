import string  # pragma: no cover
import unittest  # pragma: no cover

from unittest.mock import create_autospec  # pragma: no cover

from Service.Encryption.CaesarEncrypter import CaesarEncrypter  # pragma: no cover
from Service.Encryption.EncrypterInterface import EncrypterInterface  # pragma: no cover
from Service.Encryption.VigenereEncrypter import VigenereEncrypter  # pragma: no cover
from Service.Text.CaesarText import CaesarText  # pragma: no cover
from Service.Text.VigenereText import VigenereText  # pragma: no cover
from Service.Text.EligibleCharacters import EligibleCharacters  # pragma: no cover


class VigenereEncrypterTest(unittest.TestCase):  # pragma: no cover

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

    def test_vigenere_encrypter_encrypt_InvalidCharacter(self):
        # -------------------Parameters
        self.mock.character_list = ['A', 'B', 'C', '%']
        self.mock.cipher_character_list = []
        key = 'ABCD'
        expected_answer = ['A', 'C', 'E', "%"]
        # -------------------Encrypt
        encrypter = VigenereEncrypter(self.mock)
        encrypter.encrypt(key)
        answer = self.mock.cipher_character_list

        self.assertEqual(expected_answer, answer)

    def test_vigenere_encrypter_encrypt_OverIndex(self):
        # -------------------Parameters
        self.mock.character_list = ['A', 'B', 'C', 'D']
        self.mock.cipher_character_list = []
        key = 'ABCZ'
        expected_answer = ['A', 'C', 'E', "C"]
        # -------------------Encrypt
        encrypter = VigenereEncrypter(self.mock)
        encrypter.encrypt(key)
        answer = self.mock.cipher_character_list

        self.assertEqual(expected_answer, answer)

    def test_vigenere_encrypter_decrypt(self):
        # -------------------Parameters
        self.mock.character_list = []
        self.mock.cipher_character_list = ['A', 'B', 'C', 'D']
        key = 'ABCD'
        expected_answer = ['A', 'A', 'A', 'A']
        # -------------------Encrypt
        encrypter = VigenereEncrypter(self.mock)
        encrypter.decrypt(key)
        answer = self.mock.character_list

        self.assertEqual(expected_answer, answer)

    def test_vigenere_encrypter_decrypt_InvalidCharacter(self):
        # -------------------Parameters
        self.mock.character_list = []
        self.mock.cipher_character_list = ['A', 'B', 'C', '%']
        key = 'ABCD'
        expected_answer = ['A', 'A', 'A', "%"]
        # -------------------Encrypt
        encrypter = VigenereEncrypter(self.mock)
        encrypter.decrypt(key)
        answer = self.mock.character_list

        self.assertEqual(expected_answer, answer)

    def test_vigenere_encrypter_decrypt_OverIndex(self):
        # -------------------Parameters
        self.mock.character_list = []
        self.mock.cipher_character_list = ['A', 'B', 'C', 'D']
        key = 'ABCZ'
        expected_answer = ['A', 'A', 'A', 'E']
        # -------------------Encrypt
        encrypter = VigenereEncrypter(self.mock)
        encrypter.decrypt(key)
        answer = self.mock.character_list

        self.assertEqual(expected_answer, answer)


class CaesarEncrypterTest(unittest.TestCase):  # pragma: no cover

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

    def test_caesar_encrypter_encrypt_invalidKeyLength(self):
        # -------------------Parameters
        self.mock.character_list = ['A', 'B', 'C', 'D']
        self.mock.cipher_character_list = []
        key = 'BC'
        # -------------------Encrypt
        encrypter = CaesarEncrypter(self.mock)
        with self.assertRaises(ValueError):
            encrypter.encrypt(key)

    def test_caesar_encrypter_encrypt_InvalidCharacter(self):
        # -------------------Parameters
        self.mock.character_list = ['A', 'B', 'C', '%']
        self.mock.cipher_character_list = []
        key = 'B'
        expected_answer = ['B', 'C', 'D', '%']
        # -------------------Encrypt
        encrypter = CaesarEncrypter(self.mock)
        encrypter.encrypt(key)
        answer = self.mock.cipher_character_list

        self.assertEqual(expected_answer, answer)

    def test_caesar_encrypter_encrypt_OverIndex(self):
        # -------------------Parameters
        self.mock.character_list = ['A', 'B', 'C', 'D']
        self.mock.cipher_character_list = []
        key = 'Z'
        expected_answer = ['Z', 'A', 'B', 'C']
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

    def test_caesar_encrypter_decrypt_invalidKeyLength(self):
        # -------------------Parameters
        self.mock.character_list = []
        self.mock.cipher_character_list = ['B', 'C', 'D', 'E']
        key = 'BC'
        # -------------------Encrypt
        encrypter = CaesarEncrypter(self.mock)
        with self.assertRaises(ValueError):
            encrypter.decrypt(key)

    def test_caesar_encrypter_decrypt_InvalidCharacter(self):
        # -------------------Parameters
        self.mock.character_list = []
        self.mock.cipher_character_list = ['B', 'C', 'D', '%']
        key = 'B'
        expected_answer = ['A', 'B', 'C', '%']
        # -------------------Encrypt
        encrypter = CaesarEncrypter(self.mock)
        encrypter.decrypt(key)
        answer = self.mock.character_list

        self.assertEqual(expected_answer, answer)

    def test_caesar_encrypter_decrypt_OverIndex(self):
        # -------------------Parameters
        self.mock.character_list = []
        self.mock.cipher_character_list = ['B', 'C', 'D', 'E']
        key = 'Z'
        expected_answer = ['C', 'D', 'E', 'F']
        # -------------------Encrypt
        encrypter = CaesarEncrypter(self.mock)
        encrypter.decrypt(key)
        answer = self.mock.character_list

        self.assertEqual(expected_answer, answer)


class CharsetTest(unittest.TestCase):  # pragma: no cover

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


class EncrypterInterfaceTest(unittest.TestCase):  # pragma: no cover

    def test_interface_error(self):
        with self.assertRaises(TypeError):
            encrypter = EncrypterInterface()

    def test_key_validation(self):
        # -------------------Mock
        self.mock = create_autospec(CaesarText)
        temp = string.ascii_uppercase
        character_list = []
        for i in range(len(temp)):
            character_list.append(temp[i])
        self.mock.get_eligible_characters.return_value = character_list
        # -------------------Test
        encrypter = CaesarEncrypter(self.mock)
        self.assertEqual(encrypter.validateKey("ABCDE"), "ABCDE")
        self.assertEqual(encrypter.validateKey("ABCDe"), "ABCD")
        self.assertEqual(encrypter.validateKey("ABCD%"), "ABCD")


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
