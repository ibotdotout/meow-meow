from meow_meow.core import models
from config import config


def json_dict_to_object(json_dict, key, target_object, filters=lambda x: True):
    if key in json_dict:
        if type(json_dict[key]) is list:
            items = [target_object(item) for item in json_dict[key] if
                     filters(target_object(item))]
            return items
        else:
            return target_object(json_dict[key])
    else:
        raise NameError("Don't have {0} in json_dict".format(key))


def mapping_filters(item, keywords):
    return all([i not in item.caption.text.lower() for i in keywords])


def mapping_instagram_items(json):
    key = 'data'
    if key in json:
        keywords = config.filter_keywords
        target_object = models.InstagramItem
        filters = lambda x: mapping_filters(x, keywords)
        if keywords:
            return json_dict_to_object(json, key, target_object, filters)
        else:
            return json_dict_to_object(json, key, target_object)
