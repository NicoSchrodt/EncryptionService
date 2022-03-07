import string
import unittest

from unittest.mock import Mock, create_autospec

from Service.Encryption.VigenereEncrypter import VigenereEncrypter
from Service.Text.Vigeneretext import VigenereText


class TestClass(unittest.TestCase):
    '''
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    '''
    def test_vigenere_encrypter(self):
        mock = create_autospec(VigenereText)
        temp = string.ascii_uppercase
        character_list = []
        for i in range(len(temp)):
            character_list.append(temp[i])
        mock.get_eligible_characters.return_value = character_list
        mock.character_list = ['A', 'B', 'C', 'D']
        mock.cipher_character_list = []
        key = 'AAAA'
        expected_answer = ['A', 'B', 'C', 'D']
        encrypter = VigenereEncrypter(mock)
        encrypter.encrypt(key)
        answer = mock.cipher_character_list
        self.assertEqual(expected_answer, answer)


if __name__ == '__main__':
    unittest.main()
