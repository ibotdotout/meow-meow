def get_tags_rencently_api(tag):
    import config
    client_id = config.client_id
    api = "https://api.instagram.com/v1/tags/{tag}"\
          "/media/recent?client_id={client_id}"
    api = api.format(tag=tag, client_id=client_id)
    return api


def request_api(api_url):
    import requests
    return requests.get(api_url)
