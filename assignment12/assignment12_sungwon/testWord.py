import unittest

from word import Word

class TestWord(unittest.TestCase):

    def setUp(self):
        self.w = Word('words.txt')

    def tearDown(self):
        pass

    def testTest(self):
        self.assertEqual(self.w.test(), 'default')

    def testrandFromDB(self):
        self.assertIn(self.w.randFromDB(), self.w.words)
        self.assertIn(self.w.randFromDB(), self.w.words)
       # self.assertIn(self.w.randFromDB(), self.w.words)
       # self.assertIn(self.w.randFromDB(), self.w.words)
       # 여러개를 넣어도 testcase 통과 됨.


if __name__ == '__main__':
    unittest.main()
