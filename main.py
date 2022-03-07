from Service.Text.Vigeneretext import VigenereText
from Service.Encryption.VigenereEncrypter import VigenereEncrypter
from UnitTests.tests import TestClass


# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''
    text = VigenereText()
    text.fill_character_list("Tes&t")
    text.encrypt("EinSchluessel")
    print(f'Cipher: {text.cipher_character_list}')
    '''

    text2 = VigenereText()
    text2.fill_character_list("Tes&t")
    text2_enc = VigenereEncrypter(text2)
    text2_enc.encrypt("EinSchluessel")
    print(f'Cipher: {text2.cipher_character_list}')

    # test = TestClass()
    # test.test_vigenere_encryption()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
