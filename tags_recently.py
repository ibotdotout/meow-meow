def get_api():
    import config
    tag = config.tags[0]
    client_id = config.client_id
    api = "http://api.instagram.com/v1/tags/{tag} \
                /media/recent?client_id={client_id}"
    api = api.format(tag=tag, client_id=client_id)
    return api
