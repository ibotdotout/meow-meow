import unittest
from meow_meow.core import filters


class FiltersTest(unittest.TestCase):
    def test_can_filter_one_keyword_without_attribute(self):
        l = ['xxx', 'yyy']
        keywords = ['xxx']
        result = filters.filter_items(l, keywords)
        expected = ['yyy']
        self.assertEqual(expected, result)

    def test_can_filter_two_keyword_without_attribute(self):
        l = ['xxx', 'yyy', 'zzz', 'xxxyyy', 'zzzxxx', 'yyyzzz']
        keywords = ['xxx', 'yyy']
        result = filters.filter_items(l, keywords)
        expected = ['zzz']
        self.assertEqual(expected, result)

    def test_can_filter_one_keyword_with_attribute(self):
        l = [{'d': 'xxx'}, {'d': 'yyy'}]
        keywords = ['xxx']
        result = filters.filter_items(l, keywords, lambda x: x['d'])
        expected = [{'d': 'yyy'}]
        self.assertEqual(expected, result)

    def test_can_filter_two_keyword_with_attribute(self):
        l = [{'d': 'xxx'}, {'d': 'yyy'}, {'d': 'zzzy'}]
        keywords = ['xxx', 'yyy']
        result = filters.filter_items(l, keywords, lambda x: x['d'])
        expected = [{'d': 'zzzy'}]
        self.assertEqual(expected, result)
