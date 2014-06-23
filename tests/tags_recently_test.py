import unittest
import tags_recently


class TagsRecentlyTest(unittest.TestCase):
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

    def test_correct_api(self):
        import config
        tag = config.tags[0]
        self.assertRegexpMatches(tags_recently.get_api(), config.client_id)
        self.assertRegexpMatches(tags_recently.get_api(), tag)
