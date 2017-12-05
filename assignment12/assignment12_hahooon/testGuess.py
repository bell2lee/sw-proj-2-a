import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('apple')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), 'a _ _ _ _ ')
        self.g1.guess('p')
        self.assertEqual(self.g1.displayCurrent(), 'a p p _ _ ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'a p p l _ ')


    def testDisplayGuessed(self):
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' t ')
        self.g1.guess('q')
        self.assertEqual(self.g1.displayGuessed(), ' q t ')
        self.g1.guess('s')
        self.assertEqual(self.g1.displayGuessed(), ' q s t ')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayGuessed(), ' n q s t ')

    def testFinish(self):
        self.g1.secretWord = 'apple'
        self.g1.currentStatus = 'apple'
        self.assertTrue(self.g1.finished())

if __name__ == '__main__':
    unittest.main()
