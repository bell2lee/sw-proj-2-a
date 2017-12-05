import unittest

from hangman import Hangman

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.h = Hangman()

    def tearDown(self):
        pass

    def testdecreaseLife(self):
        self.assertEqual(self.h.remainingLives, 6)
        self.h.decreaseLife()
        self.assertEqual(self.h.remainingLives, 5)
        self.h.decreaseLife()
        self.assertEqual(self.h.remainingLives, 4)
        self.h.decreaseLife()
        self.assertEqual(self.h.remainingLives, 3)
        self.h.decreaseLife()
        self.assertEqual(self.h.remainingLives, 2)
        self.h.decreaseLife()
        self.assertEqual(self.h.remainingLives, 1)
        self.h.decreaseLife()
        self.assertEqual(self.h.remainingLives, 0)

    def testcurrentShape(self):

        self.assertEqual(self.h.currentShape(), self.h.text[6])
        self.h.decreaseLife()
        self.assertEqual(self.h.currentShape(), self.h.text[5])
        self.h.decreaseLife()
        self.assertEqual(self.h.currentShape(), self.h.text[4])
        self.h.decreaseLife()
        self.assertEqual(self.h.currentShape(), self.h.text[3])
        self.h.decreaseLife()
        self.assertEqual(self.h.currentShape(), self.h.text[2])
        self.h.decreaseLife()
        self.assertEqual(self.h.currentShape(), self.h.text[1])
        self.h.decreaseLife()
        self.assertEqual(self.h.currentShape(), self.h.text[0])


if __name__ == '__main__':
    unittest.main()