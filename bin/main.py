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
        from meow_meow.render import index
        json_data = json.load(json_file)
        html = index.render(json_data)
        write_html(html, 'index.html')


def run():
    from meow_meow.render import index
    json = index.query_json()
    dump_json(json)
    html = index.render(json)
    write_html(html, 'index.html')

if __name__ == '__main__':
    run()
    # debug()
