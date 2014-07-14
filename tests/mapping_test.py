import unittest
import mapping


class MappingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import json
        with open('tests/request_test.json') as json_data:
            cls.json = json.load(json_data)
            import models
            cls.key = 'data'
            cls.target_object = models.InstragramItem

    def test_json_dict_to_object_len_correct(self):
        expected_result = len(self.json['data'])
        result = mapping.json_dict_to_object(self.json, self.key,
                                             self.target_object)
        result = len(result)
        self.assertEqual(expected_result, result)

    def test_json_dict_to_object_data_correct(self):
        import models
        l = [0, 1, 3, 5, -7, -1]
        for i in l:
            expected_result = models.InstragramItem(self.json['data'][i])
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
