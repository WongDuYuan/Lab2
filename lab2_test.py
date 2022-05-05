import unittest
import lab2


class MyTestCase(unittest.TestCase):
    def test_Input(self):
        expected = [11, 22, 33, 44]
        string = "11, 22, 33, 44"
        result = lab2.get_user_input_test(string)
        self.assertEqual(result, expected)  # add assertion here
    def test_Average(self):
        expected = 30
        temp = [10, 20, 30, 40, 50]
        result = lab2.calc_average_temperature(temp)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
