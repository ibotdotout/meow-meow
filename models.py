class User():
    def __init__(self, json):
        self.username = json['username']
        self.profile_picture = json['profile_picture']
        self.full_name = json['full_name']


class Image():
    def __init__(self, json):
        self.url = json['url']
        self.width = json['width']
        self.height = json['height']


class ImageResolutions():
    def __init__(self, json):
        self.low = Image(json['low_resolution'])
        self.thumbnail = Image(json['thumbnail'])
        self.standard = Image(json['standard_resolution'])


class Caption():
    def __init__(self, json):
        self.text = json['text']


class InstragramItem():
    def __init__(self, json):
        self.user = User(json['user'])
        self.caption = Caption(json['caption'])
        self.images = ImageResolutions(json['images'])
