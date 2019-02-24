import unittest

from pubmed.example_mod import ExampleMod


class ExampleModTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example_mod(self):
        clsobj = ExampleMod()
        self.assertEqual(clsobj.add(), 21)


if __name__ == '__main__':
    # Run tests with the warning such as below ignored (not shown).
    # InsecureRequestWarning: Unverified HTTPS request
    # ResourceWarning: unclosed <ssl.SSLSocket fd=5, ...
    unittest.main(warnings='ignore')
