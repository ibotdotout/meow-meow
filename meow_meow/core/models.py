class User():
    def __init__(self, json):
        self.username = json.get('username')
        self.profile_picture = json.get('profile_picture')
        self.full_name = json.get('full_name')


class Image():
    def __init__(self, json):
        self.url = json.get('url')
        self.width = json.get('width')
        self.height = json.get('height')


class ImageResolutions():
    def __init__(self, json):
        self.low = Image(json.get('low_resolution'))
        self.thumbnail = Image(json.get('thumbnail'))
        self.standard = Image(json.get('standard_resolution'))


class Caption():
    def __init__(self, json):
        if json:
            self.text = json.get('text')
        else:
            self.text = ""


class InstagramItem():
    def __init__(self, json):
        self.user = User(json.get('user'))
        self.caption = Caption(json.get('caption'))
        self.images = ImageResolutions(json.get('images'))
