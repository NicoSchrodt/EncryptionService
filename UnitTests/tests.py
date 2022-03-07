import unittest

from unittest.mock import Mock

from Service.Encryption import VigenereEncrypter


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
    def test_vigenere_encryption(self):
        mock = Mock()
        mock.character_list = ['a', 'b', 'c', 'd']
        #test_string = ['a', 'b', 'c', 'd']
        key = 'aaaa'
        expected_answer = ['A', 'B', 'C', 'D']
        answer = VigenereEncryption.encryptVig(mock, key)
        self.assertEqual(expected_answer, answer)


if __name__ == '__main__':
    unittest.main()
