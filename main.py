import api


def get_items(json):
    import mapping
    return mapping.mapping_instragram_items(json)


def recently_tag(tags):
    tags_api = api.get_tags_recently_api(tags)
    print(tags_api)
    return api.request_api(tags_api)


def run():
    tags = 'cat'
    respone = recently_tag(tags)
    items = get_items(respone.json)
    for i in items:
        print(i.user)
