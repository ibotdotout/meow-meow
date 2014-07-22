import unittest
from unittest import mock
from meow_meow.core import mapping


class MappingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import json
        import os.path
        filepath = os.path.join(os.path.dirname(__file__),
                                'request_sample.json')
        with open(filepath, 'r') as json_data:
            cls.json = json.load(json_data)
            cls.key = 'data'

    @mock.patch('meow_meow.core.models')
    def test_mapping_instragram_items(self, mock_target_obj):
        mock_target_obj.InstragramItem = lambda x: x
        result = mapping.mapping_instragram_items(self.json)
        self.assertTrue(len(result) > 0)

    def test_json_dict_to_object_len_correct(self):
        expected_result = len(self.json[self.key])
        result = mapping.json_dict_to_object(self.json, self.key, lambda x: x)
        result = len(result)
        self.assertEqual(expected_result, result)

    def test_json_dict_to_object_data_correct(self):
        expected = self.json[self.key]
        result = mapping.json_dict_to_object(self.json, self.key, lambda x: x)
        self.assertEqual(expected, result)

    def test_json_dict_to_object_with_not_list(self):
        expected = "1403564068967133"
        result = mapping.json_dict_to_object(self.json['pagination'],
                                             'next_max_tag_id', str)
        self.assertEqual(expected, result)

    def test_json_dict_to_object_raise_error(self):
        json = {'meta': {'code': 200}}
        self.assertRaises(NameError, mapping.json_dict_to_object, json,
                          self.key, dict())
