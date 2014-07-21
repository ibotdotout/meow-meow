import os

# Configuration from Environment Variables if can't load config.ini
# you can make you own configuration from config.ini.sample

if os.path.isfile("config.ini"):
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    client_id = config.get('DEFAULT', 'client_id')
    tags = [i.strip() for i in config.get('DEFAULT', 'tags').split(',')]
else:
    client_id = os.environ['CLIENT_ID']
    tags = os.environ['TAGS']

print(client_id, tags)
