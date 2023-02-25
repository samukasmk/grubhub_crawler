def get_restaurant_id_from_url(url):
    return url.split('/')[-1]


def normalize_price_value(original_price_value):
    return original_price_value / 100
