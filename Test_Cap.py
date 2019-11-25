import unittest
import Cap

class Test_Cap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = Cap.cap_word(text)
        self.assertEqual(result , 'Python')

    def test_multiple_words(self):
        text = 'learn python'
        result = Cap.cap_word(text)
        self.assertEqual(result,'Monty Python')

if __name__=='__main__':
    unittest.main()