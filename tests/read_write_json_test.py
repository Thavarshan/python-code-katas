from src.katas.read_write_json import write_to_json_file, read_from_json_file
import unittest


class ReadWriteJsonTest(unittest.TestCase):

    _data = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }

    def test_can_write_given_data_to_json_file_in_proper_json_format(self):
        json_file = 'tests/fixtures/data_file.json'
        write_to_json_file(self._data, json_file)
        self.assertEqual(self._data, read_from_json_file(json_file))
