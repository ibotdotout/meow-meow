def get_api():
    import config
    tag = config.tags[0]
    client_id = config.client_id
    api = "https://api.instagram.com/v1/tags/{tag}"\
          "/media/recent?client_id={client_id}"
    api = api.format(tag=tag, client_id=client_id)
    return api


def request_api_json():
    import requests
    return requests.get(get_api()).json()
