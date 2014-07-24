def has_keywords(text, keywords):
    return any([i in text.lower() for i in keywords])


def filter_items(items, keywords=None, attribute=lambda x: x):
    result = []
    if keywords:
        for i in items:
            if not has_keywords(attribute(i), keywords):
                result.append(i)
    else:
        result = items
    return result
