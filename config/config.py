import os

# Configuration from Environment Variables if can't load config.ini
# you can make you own configuration from config.ini.sample


CONFIG_PATH = "config/config.ini"
client_id = os.environ.get('CLIENT_ID')
raw_tags = os.environ.get('TAGS')
raw_filter_keywords = os.environ.get('FILTER_KEYWORDS')


def remove_quote(x):
    """ remove single and double quotes """
    return x.replace('"', '').replace("'", "")


def config_from_config_dot_ini(CONFIG_PATH):
    """ load configuration from config.ini """
    import configparser
    global client_id, raw_tags, raw_filter_keywords
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    client_id = config.get('DEFAULT', 'client_id')
    raw_filter_keywords = config.get('DEFAULT', 'filter_keywords')
    raw_tags = config.get('DEFAULT', 'tags')


def config_ini_exists(CONFIG_PATH):
    """ is config.ini exists """
    return os.path.isfile(CONFIG_PATH)

if config_ini_exists(CONFIG_PATH):
    config_from_config_dot_ini(CONFIG_PATH)

tags = [i.strip() for i in remove_quote(raw_tags).split(',')]
filter_keywords = [i.strip() for i in remove_quote(raw_filter_keywords)
                   .split(',')]
