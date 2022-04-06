import unittest

from GBP.Proc import Proc


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_Proc(self):
        process = Proc("Process 1")
        process.init()
        process.delete('req')
        process.external()
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
