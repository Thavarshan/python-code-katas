import os
import unittest
from src.katas.env_secret_generator import SecretKeyGenerator


class TestSecretKeyGenerator(unittest.TestCase):

    def test_find_string_in_file(self):
        skey_generator = SecretKeyGenerator('tests/fixtures/content.txt')
        self.assertTrue(skey_generator.check_str_in_lines('Hello'))
        self.assertFalse(skey_generator.check_str_in_lines('hello'))

    def test_make_key_and_value(self):
        skey_generator = SecretKeyGenerator()
        self.assertTrue(('SECRET_KEY' in skey_generator.make_key_and_value()))

    def test_write_key_to_file(self):
        env_file = 'tests/fixtures/.env'
        self.create_dummy_file(env_file)

        skey_generator = SecretKeyGenerator(env_file)
        self.assertFalse(skey_generator.check_str_in_lines('SECRET_KEY'))
        skey_generator.write_to_file()
        self.assertTrue(skey_generator.check_str_in_lines('SECRET_KEY'))
        os.remove(env_file)

    def create_dummy_file(self, file_name):
        with open(file_name, 'w+') as file:
            pass


if __name__ == '__main__':
    unittest.main()
