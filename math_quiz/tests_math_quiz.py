import unittest
from math_quiz import random_int, random_math_operator, create_math_quiz


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_math_operator(self):
        # Test if random operator generated is any of ['+', '-', '*']
        rand_operator_set = set()
        for _ in range(1000):   # Test a large number of generated operators
            rand_operator_set.add(random_math_operator())
        
        # there should only be the 3 defined operators generated
        self.assertEqual(len(rand_operator_set), 3)

        self.assertIn('+', rand_operator_set)   # check if '+' is generated
        self.assertIn('-', rand_operator_set)   # check if '-' is generated
        self.assertIn('*', rand_operator_set)   # check if '*' is generated

    def test_create_math_quiz(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 7, '*', '3 * 7', 21),
                (6, 4, '-', '6 - 4', 2),
                (1, 10, '-', '1 - 10', -9)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                generated_problem, generated_answer = create_math_quiz(num1, num2, operator)
                self.assertEqual(generated_problem, expected_problem)
                self.assertEqual(generated_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
