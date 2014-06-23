import unittest
import models


class ModelsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import tags_recently
        cls.request = tags_recently.request_api()
        cls.json = cls.request.json()
        cls.json = cls.json['data'][0]

    def test_user_model(self):
        json = self.json['user']
        user = models.User(json)
        self.assertEqual(user.username, json['username'])
        self.assertEqual(user.profile_picture, json['profile_picture'])
        self.assertEqual(user.full_name, json['full_name'])

    def test_image_model(self):
        json = self.json['images']['thumbnail']
        image = models.Image(json)
        self.assertEqual(image.url, json['url'])
        self.assertEqual(image.width, json['width'])
        self.assertEqual(image.height, json['height'])

    def test_image_resolutions_model(self):
        json = self.json['images']
        images = models.ImageResolutions(json)
        self.assertEqual(images.standard.url,
                         json['standard_resolution']['url'])
        self.assertEqual(images.thumbnail.url, json['thumbnail']['url'])
        self.assertEqual(images.low.url, json['low_resolution']['url'])

    def test_caption_model(self):
        json = self.json['caption']
        caption = models.Caption(json)
        self.assertEqual(caption.text, json['text'])

    def test_instragram_item_model(self):
        json = self.json
        item = models.InstragramItem(json)

        # caption model
        caption_json = json['caption']
        self.assertEqual(item.caption.text, caption_json['text'])

        # image resolutions model
        images_json = json['images']
        self.assertEqual(item.images.standard.url,
                         images_json['standard_resolution']['url'])
        self.assertEqual(item.images.thumbnail.url,
                         images_json['thumbnail']['url'])
        self.assertEqual(item.images.low.url,
                         images_json['low_resolution']['url'])

        # user model
        user_json = json['user']
        self.assertEqual(item.user.username, user_json['username'])
        self.assertEqual(item.user.profile_picture,
                         user_json['profile_picture'])
        self.assertEqual(item.user.full_name, user_json['full_name'])
