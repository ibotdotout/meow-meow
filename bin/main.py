#!/usr/bin/env python


def dump_json(json_data):
    import json
    with open('lastest_request.json', 'w') as outfile:
        json.dump(json_data, outfile)


def write_html(html, dst_path):
    with open(dst_path, 'w') as file:
        file.write(html)


def debug():
    with open('lastest_request.json', 'r') as json_file:
        import json
        from meow_meow.core import mapping
        json_data = json.load(json_file)
        items = mapping.mapping_instragram_items(json_data)
        if items:
            print("look the cats")
        else:
            print("Can't get items")


def run():
    from meow_meow.render import index
    response = index.quiry()
    dump_json(response.json())
    html = index.render(response)
    write_html(html, 'index.html')

if __name__ == '__main__':
    run()
