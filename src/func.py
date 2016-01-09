import unittest

def ascii2binary(word):
    binary_list = list(map(hex, map(ord, word)))
    return binary_list

def binary2ascii(binary_list):
    word = ""
    for i in binary_list:
        word += chr(int(i, 16))
    return word

class TestSequenceFunction(unittest.TestCase):
    '''
    unittestモジュールを使ったPythonのテストクラス
    '''
    
    def test_encode_binary(self):
        word = "hello"
        binary_list = ['0x68', '0x65', '0x6c', '0x6c', '0x6f']
        self.assertEqual(ascii2binary(word),binary_list)

    def test_decode_word(self):
        word = "hello"
        binary_list = ['0x68', '0x65', '0x6c', '0x6c', '0x6f']
        self.assertEqual(binary2ascii(binary_list),word)

if __name__ == "__main__":
    unittest.main()
