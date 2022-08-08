import Scanner
import unittest


class ScannerTestCases(unittest.TestCase):

    def test_string(self):
        a = Scanner.Scanner("This is a test")
        self.assertEqual(["test"], a.rawTokens[-1])

    def test_list(self):
        a = Scanner.Scanner(['this is a test', 'and "another"', 'and a third'])
        self.assertEqual(["third"], a.rawTokens[-1])

    def test_bad_data(self):
        try:
            a = Scanner.Scanner(5) # neither a list nor a string
            fail = False
        except ValueError as ex:
            fail = True

            self.assertTrue(fail)