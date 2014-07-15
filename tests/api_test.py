import unittest
from unittest import mock
from core import api


class TagsRecentlyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        import os.path
        import json
        import requests

        filepath = os.path.join(os.path.dirname(__file__),
                                'request_sample.json')
        cls.tag = 'cat'
        cls.tags_api = api.get_tags_recently_api(cls.tag)
        with open(filepath, 'r') as json_file:
            json_data = json.load(json_file)
            with mock.patch('requests.get') as cls.mock_requests_get:
                cls.mock_requests_get.return_value = mock_response = \
                    mock.Mock(spec=requests.models.Response)
                mock_response.json.return_value = json_data
                cls.request = api.request_api(cls.tags_api)

    def test_called_api_request_api(self):
        self.mock_requests_get.assert_called_with(self.tags_api)

    def test_has_config_file(self):
        import os.path
        path = os.path.dirname(os.path.dirname(__file__))
        filepath = os.path.join(path, 'config.py')
        self.assertTrue(os.path.isfile(filepath),
                        "please make your config first")

    def test_config_has_client_id(self):
        import config
        self.assertTrue(config.client_id,
                        "put your client id in config file")

    def test_config_has_tags(self):
        import config
        self.assertTrue(config.tags,
                        "put your tags id in config file")

    def test_can_get_api(self):
        import config
        tag = self.tag
        api_url = self.tags_api
        self.assertRegexpMatches(api_url, "https:", "use api with https")
        self.assertRegexpMatches(api_url, config.client_id)
        self.assertRegexpMatches(api_url, tag)

    def test_request_api_get_something(self):
        import requests
        self.assertTrue(isinstance(self.request, requests.models.Response))

    def test_request_not_get_error(self):
        if self.request:
            json = self.request.json()
            self.assertEqual(json['meta']['code'], 200)
