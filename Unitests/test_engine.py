import unittest

from Const.Const import REQ
from GBP.Proc import Proc


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_Proc(self):
        process = Proc("Process 1")
        process.init()
        print(process.inputEvents)
        process.write(REQ, False)
        print(process.inputEvents)
        process.deleteEvent('req')
        process.external()
        self.assertEqual(True, True)

    def test2(self):
        dict = {}
        print(dict)
        dict["nom"] = "Pascal"
        print(dict)
        dict["Prenom"] = "Classen"
        print(dict)


if __name__ == '__main__':
    unittest.main()
