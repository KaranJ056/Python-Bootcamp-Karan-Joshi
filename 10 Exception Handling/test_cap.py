import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.capitalize_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'karan joshi'
        result = cap.capitalize_text(text)
        self.assertEqual(result, 'Karan Joshi')

if __name__ == "__main__":
    unittest.main()
