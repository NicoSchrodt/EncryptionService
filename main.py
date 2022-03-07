from Service.Text.Vigeneretext import VigenereText
from Service.Encryption.VigenereEncrypter import VigenereEncrypter

if __name__ == '__main__':
    text2 = VigenereText()
    text2.fill_character_list("Tes&t")
    text2_enc = VigenereEncrypter(text2)
    text2_enc.encrypt("EinSchluessel")
    print(f'Cipher: {text2.cipher_character_list}')
