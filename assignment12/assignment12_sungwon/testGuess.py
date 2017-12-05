import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ _ _ _ _ ') # 초기 상태 검사
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('o')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' ') # 초기 상태 검사
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a t u ')

if __name__ == '__main__':
    unittest.main()
