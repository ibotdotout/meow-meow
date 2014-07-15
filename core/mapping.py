def json_dict_to_object(json_dict, key, target_object):
    if key in json_dict:
        if type(json_dict[key]) is list:
            items = [target_object(item) for item in json_dict[key]]
            return items
        else:
            return target_object(json_dict[key])
    else:
        raise NameError("Don't have {0} in json_dict".format(key))


def mapping_instragram_items(json):
    from core import models
    key = 'data'
    if key in json:
        target_object = models.InstragramItem
        return json_dict_to_object(json, key, target_object)