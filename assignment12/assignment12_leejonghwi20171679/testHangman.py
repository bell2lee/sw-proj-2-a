import unittest

from hangman import Hangman

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.h = Hangman()

    def tearDown(self):
        pass
    def testCurrentShape(self):
        for i in range(len(self.h.text)-1, 0, -1):
            self.assertEqual(self.h.currentShape(), self.h.text[i])
            if not i == 0 : self.h.decreaseLife()

if __name__ == '__main__':
    unittest.main()
