import unittest

from guess import Guess
from hangman import Hangman

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ a u _ t ')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a t u ')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayGuessed(), ' a n t u ')

if __name__ == '__main__':
    unittest.main()
