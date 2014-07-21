import unittest
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
            from meow_meow.core import models
            cls.key = 'data'
            cls.target_object = models.InstragramItem

    def test_mapping_instragram_items(self):
        result = mapping.mapping_instragram_items(self.json)
        self.assertTrue(len(result) > 0)

    def test_json_dict_to_object_len_correct(self):
        expected_result = len(self.json[self.key])
        result = mapping.json_dict_to_object(self.json, self.key,
                                             self.target_object)
        result = len(result)
        self.assertEqual(expected_result, result)

    def test_json_dict_to_object_data_correct(self):
        from meow_meow.core import models
        l = [0, 1, 3, 5, -7, -1]
        for i in l:
            expected_result = models.InstragramItem(self.json[self.key][i])
            result = mapping.json_dict_to_object(self.json, self.key,
                                                 self.target_object)
            result = result[i]
            self.assertEqual(expected_result.caption.text, result.caption.text)
            self.assertEqual(expected_result.images.low.url,
                             result.images.low.url)
            self.assertEqual(expected_result.user.username,
                             result.user.username)

    def test_json_dict_to_object_with_not_list(self):
        expected = "1403564068967133"
        result = mapping.json_dict_to_object(self.json['pagination'],
                                             'next_max_tag_id', str)
        self.assertEqual(expected, result)

    def test_json_dict_to_object_raise_error(self):
        json = {'meta': {'code': 200}}
        self.assertRaises(NameError, mapping.json_dict_to_object, json,
                          self.key, self.target_object)
