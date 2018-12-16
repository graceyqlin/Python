import unittest
from stringutility import StringUtility

class TestStringUtility(unittest.TestCase):
    
    def setUp(self):
        self.stringUtil = StringUtility()
    
    def test_reverse(self):
        self.assertEqual(self.stringUtil.reverse("Test String"), "gnirtS tseT")
        self.assertEqual(self.stringUtil.reverse("Otto"), "ottO")
        self.assertEqual(self.stringUtil.reverse(""), "")
        self.assertEqual(self.stringUtil.reverse("  "), "  ")
        
    def test_char_frequency(self):
        self.assertEqual(self.stringUtil.char_frequency("Test String", "t"), 2)
        
    def test_is_palindrone(self):
        self.assertTrue(self.stringUtil.is_palindrone("otto"))


if __name__ == "__main__":
    testStringUtil = TestStringUtility()
    suite = unittest.TestLoader().loadTestsFromModule(testStringUtil)
    unittest.TextTestRunner().run(suite)