import os

# Configuration from Environment Variables if can't load config.ini
# you can make you own configuration from config.ini.sample


CONFIG_PATH = "config/config.ini"
client_id = os.environ.get('CLIENT_ID')
raw_tags = os.environ.get('TAGS')


def remove_quote(tags):
    """ remove single and double quotes """
    return raw_tags.replace('"', '').replace("'", "")


def config_from_config_dot_ini(CONFIG_PATH):
    """ load configuration from config.ini """
    import configparser
    global client_id, raw_tags
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    client_id = config.get('DEFAULT', 'client_id')
    raw_tags = config.get('DEFAULT', 'tags')


def config_ini_exists(CONFIG_PATH):
    """ is config.ini exists """
    return os.path.isfile(CONFIG_PATH)

if config_ini_exists(CONFIG_PATH):
    config_from_config_dot_ini(CONFIG_PATH)

tags = [i.strip() for i in raw_tags.split(',')]
