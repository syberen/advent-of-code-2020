import unittest

from validator import PassportValidator


class TestCount(unittest.TestCase):
    def test_count_valid_passports_by_fields_present(self):
        """ Assert that count_valid_passports_by_fields_present returns the right number for given input """
        validator = PassportValidator('test_fixtures/input_fields.txt')

        self.assertEqual(
            validator.count_valid_passports_by_fields_present(), 2)

    def test_count_valid_passports_with_value_validation(self):
        """ Assert that count_valid_passports_with_value_validation returns the right number for given input """
        validator = PassportValidator('test_fixtures/input_values.txt')

        self.assertEqual(
            validator.count_valid_passports_with_value_validation(), 4)


if __name__ == '__main__':
    unittest.main()
