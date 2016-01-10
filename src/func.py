import unittest, functools

def ascii2binary(word):
    binary_list = list(map(hex, map(ord, word)))
    return binary_list

def binary2ascii(binary_list):
    word = ""
    for i in binary_list:
        word += chr(int(i, 16))
    return word

def encryption(binary,add_num):
    decimal = int(binary, 16)
    return decimal + add_num

def decode(decimal,diff_num):
    binary = decimal - diff_num
    return hex(binary)

def encryption_list(binary_list, add_num):
    return list(map(functools.partial(encryption,add_num=add_num),binary_list))

def decode_list(cipher_list, diff_num):
    return list(map(functools.partial(decode,diff_num=diff_num),cipher_list))

def bind_cipher(cipher_list):
    return 'x'.join(list(map(str,cipher_list)))

def split_cipher(cipher):
    return list(map(int,cipher.split('x')))

class TestSequenceFunction(unittest.TestCase):
    '''
    unittestモジュールを使ったPythonのテストクラス
    '''
   
    key_num = 4
    word = "hello"
    binary_list = ['0x68', '0x65', '0x6c', '0x6c', '0x6f']
    cipher_list = [108, 105, 112, 112, 115]
    cipher = '108x105x112x112x115'

    def test_encode_binary(self):
        self.assertEqual(ascii2binary(self.word),self.binary_list)

    def test_decode_word(self):
        self.assertEqual(binary2ascii(self.binary_list),self.word)

    def test_encryptiom(self):
        self.assertEqual(encryption(self.binary_list[0],self.key_num),self.cipher_list[0])

    def test_decode(self):
        self.assertEqual(decode(self.cipher_list[0],self.key_num),self.binary_list[0])

    def test_encryption_list(self):
        self.assertEqual(encryption_list(self.binary_list,self.key_num),self.cipher_list)

    def test_decode_list(self):
        self.assertEqual(decode_list(self.cipher_list,self.key_num),self.binary_list)
        
    def test_bind_list(self):
        self.assertEqual(bind_cipher(self.cipher_list),self.cipher)

    def test_split_list(self):
        self.assertEqual(split_cipher(self.cipher),self.cipher_list)

if __name__ == "__main__":
    unittest.main()
