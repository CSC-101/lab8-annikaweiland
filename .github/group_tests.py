import unittest
import group


class MyTestCase(unittest.TestCase):

#TASK 1 TESTS
    def test_groups_of_3(self):
        input = [4, 5, 6, 4, 2, 6, 5]
        expected = [[4, 5, 6], [4, 2, 6], [5]]
        result = group.groups_of_3(input)
        self.assertEqual(result, expected)

    def test_groups_of_3(self):
        input = [4, 5, 2, 1, 5, 3, 8, 10]
        expected = [[4, 5, 2], [1, 5, 3], [8, 10]]
        result = group.groups_of_3(input)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
