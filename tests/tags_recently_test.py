import unittest
import tags_recently


class TagsRecentlyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = tags_recently.request_api()

    def test_has_config_file(self):
        import os.path
        fname = "config.py"
        self.assertTrue(os.path.isfile(fname), "please make your config first")

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
        tag = config.tags[0]
        api = tags_recently.get_api()
        self.assertRegexpMatches(api, "https:", "use api with https")
        self.assertRegexpMatches(api, config.client_id)
        self.assertRegexpMatches(api, tag)

    def test_request_api_get_something(self):
        import requests
        self.assertTrue(isinstance(self.request, requests.models.Response))

    def test_request_not_get_error(self):
        if self.request:
            json = self.request.json()
            self.assertEqual(json['meta']['code'], 200)
