import os

# Configuration from Environment Variables if can't load config.ini
# you can make you own configuration from config.ini.sample

CONFIG_PATH = "config/config.ini"

if os.path.isfile(CONFIG_PATH):
    import configparser
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    client_id = config.get('DEFAULT', 'client_id')
    tags = [i.strip() for i in config.get('DEFAULT', 'tags').split(',')]
else:
    client_id = os.environ['CLIENT_ID']
    tags = [i.strip() for i in os.environ['TAGS'].split(',')]
