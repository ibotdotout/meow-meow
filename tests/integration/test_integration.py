import unittest
from bin import main


class IntegrationTest(unittest.TestCase):
    def test_run(self):
        import os
        main.run()
        self.assertTrue(os.path.isfile("index.html"))
        self.assertTrue(os.path.isfile("lastest_request.json"))
