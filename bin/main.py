def dump_json(json_data):
    import json
    with open('lastest_request.json', 'w') as outfile:
        json.dump(json_data, outfile)


def get_items(json):
    from core import mapping
    return mapping.mapping_instragram_items(json)


def recently_tag(tags):
    from core import api
    tags_api = api.get_tags_recently_api(tags)
    return api.request_api(tags_api)

def generate_mako_template(items):
    from mako.lookup import TemplateLookup
    mylookup = TemplateLookup(directories=['templates'],
                              module_directory='/tmp/mako_modules',
                              input_encoding='utf-8')
    mytemplate = mylookup.get_template("index.mako")
    return mytemplate.render(items=items)


def write_html(items):
    html = generate_mako_template(items)
    with open('index.html', 'w') as file:
        file.write(html)


def tags_from_config():
    import config
    return config.tags


def print_result(items):
    if items:
        print("look the cats")
        write_html(items)
    else:
        print("Can't get items")


def debug():
    with open('lastest_request.json', 'r') as json_file:
        import json
        json_data = json.load(json_file)
        items = get_items(json_data)
        print_result(items)


def run():
    tags = tags_from_config()
    tags = tags[0]
    respone = recently_tag(tags)
    dump_json(respone.json())
    items = get_items(respone.json())
    print_result(items)

if __name__ == '__main__':
    run()
    # debug()
