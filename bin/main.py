def get_items(json):
    from core import mapping
    return mapping.mapping_instragram_items(json)


def recently_tag(tags):
    from core import api
    tags_api = api.get_tags_recently_api(tags)
    return api.request_api(tags_api)


def write_html(items):
    with open('index.html', 'w') as file:
        file.write('<html>')
        file.write('<body>')
        for i in items:
            img = "<img src={0}></img>".format(i.images.thumbnail.url)
            file.write(img)
        file.write('</body>')
        file.write('</html>')


def tags_from_config():
    import config
    return config.tags


def run():
    tags = tags_from_config()
    tags = tags[0]
    respone = recently_tag(tags)
    items = get_items(respone.json())
    if items:
        print("look the cats")
        write_html(items)
    else:
        print("Can't get items")

if __name__ == '__main__':
    run()
