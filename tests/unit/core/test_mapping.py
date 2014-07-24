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

    @mock.patch('meow_meow.core.models.InstagramItem')
    @mock.patch('config.config.filter_keywords',
                new_callable=mock.PropertyMock(return_value=[]))
    def test_mapping_instagram_items(self, mock_keywords,
                                     mock_ig_item):
        mock_ig_item.side_effect = lambda x: x
        result = mapping.mapping_instagram_items(self.json)
        self.assertTrue(len(result) >= 0)

    @mock.patch('meow_meow.core.models.InstagramItem')
    @mock.patch('config.config.filter_keywords',
                new_callable=mock.PropertyMock(return_value=['cat', 'kitty']))
    @mock.patch('meow_meow.core.mapping.mapping_filters')
    def test_mapping_instagram_items_with_filters(self, mock_filters,
                                                  mock_keywords, mock_ig_item):
        mock_ig_item.side_effect = lambda x: x
        mock_filters.side_effect = \
            lambda x, keywords: all([i not in x['caption']['text'].lower()
                                     for i in keywords])
        result = mapping.mapping_instagram_items(self.json)
        self.assertEqual(len(result), 4)

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

    def test_josn_dict_to_object_can_filter_item(self):
        expected = 0
        filters = lambda x: False
        result = mapping.json_dict_to_object(self.json, 'data', dict, filters)
        self.assertEqual(len(result), expected)
