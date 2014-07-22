def get_items(json):
    from meow_meow.core import mapping
    return mapping.mapping_instagram_items(json)


def recently_tag(tags):
    from meow_meow.core import api
    tags_api = api.get_tags_recently_api(tags)
    return api.request_api(tags_api)


def generate_mako_template(items):
    from meow_meow.render import config
    mytemplate = config.mako_lookup.get_template("index.mako")
    return mytemplate.render(items=items)


def tags_from_config():
    from config import config
    return config.tags


def query():
    tags = tags_from_config()
    tags = tags[0]
    response = recently_tag(tags)
    return response


def render(response=query()):
    items = get_items(response.json())
    return generate_mako_template(items)

if __name__ == '__main__':
    render()
