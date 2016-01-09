import unittest

def add2num(x,y):
    return x + y

class TestSequenceFunction(unittest.TestCase):
    '''
    unittestモジュールを使ったPythonのテストクラス
    '''
    
    def test_equal(self):
        x = 1
        y = 2
        self.assertEqual(add2num(x,y),3)

if __name__ == "__main__":
    unittest.main()
