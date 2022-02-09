import unittest
import lesson_199


class GameTest(unittest.TestCase):

    def test_correct_guess(self):
        result = lesson_199.guess_check(5, 5)
        self.assertTrue(result)

    def test_wrong_guess(self):
        result = lesson_199.guess_check(5, 4)
        self.assertFalse(result)

    def test_not_in_range(self):
        result = lesson_199.guess_check(35, 4)
        self.assertFalse(result)

    def test_wrong_type(self):
        result = lesson_199.guess_check('*', 10)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
