import argparse
from grubhub.crawler.formaters import get_restaurant_id_from_url


def grubhub_restaurant_url(url):
    restaurant_id = get_restaurant_id_from_url(url)
    if not restaurant_id.isdigit():
        raise ValueError('Value ({url_arg}) has no valid restaurant_id')
    return url


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description='Crawler for GrubHub Restaurants.')
    parser.add_argument('-u', '--urls', required=True, type=grubhub_restaurant_url, nargs='+',
                        help=('URLs from GrubHub Restaurants (requirements: '
                              'it can be more than one, '
                              'it must have the restaurant_id number on final). '
                              'Example: --urls '
                              'https://www.grubhub.com/restaurant/.../3024935 '
                              'https://www.grubhub.com/restaurant/.../3235140 '
                              'https://www.grubhub.com/restaurant/.../3159434'))
    parser.add_argument('--verbose-csv', action='store_true',
                        help='Add extra fields to csv to compare data crossing and data origin')
    return parser.parse_args()
