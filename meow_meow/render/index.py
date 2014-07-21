def get_items(json):
    from meow_meow.core import mapping
    return mapping.mapping_instragram_items(json)


def recently_tag(tags):
    from meow_meow.core import api
    tags_api = api.get_tags_recently_api(tags)
    return api.request_api(tags_api)


def generate_mako_template(items):
    from mako.lookup import TemplateLookup
    mylookup = TemplateLookup(directories=['templates'],
                              module_directory='/tmp/mako_modules',
                              input_encoding='utf-8')
    mytemplate = mylookup.get_template("index.mako")
    return mytemplate.render(items=items)


def tags_from_config():
    from config import config
    return config.tags


def print_result(items):
    if items:
        print("look the cats")
    else:
        print("Can't get items")


def render():
    tags = tags_from_config()
    tags = tags[0]
    respone = recently_tag(tags)
    items = get_items(respone.json())
    print_result(items)
    return generate_mako_template(items)

if __name__ == '__main__':
    render()
