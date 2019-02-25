import unittest

from pubmed.package1.example_mod2 import ExampleMod2


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

    def test_example_mod2(self):
        clsobj = ExampleMod2()
        self.assertEqual(clsobj.compose(), 'cat catches mouse.')


if __name__ == '__main__':
    # Run tests with the warning such as below ignored (not shown).
    # InsecureRequestWarning: Unverified HTTPS request
    # ResourceWarning: unclosed <ssl.SSLSocket fd=5, ...
    unittest.main(warnings='ignore')
