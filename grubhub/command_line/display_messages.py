from datetime import datetime

def display_title():
    print('[GrubHub Crawler]')
    print()
    print('Getting restaurants data:')


def display_horizontal_rule():
    print('-' * 160)


def display_restaurants_info(crawled_restaurants):
    for crawled_restaurant in crawled_restaurants:
        display_horizontal_rule()
        print(f'-> ({crawled_restaurant["async_index"]}) Restaurant URL: {crawled_restaurant["restaurant_url"]}')
        for restaurant_key, restaurant_value in crawled_restaurant["restaurant_info"].items():
            print(f'       {restaurant_key}: {restaurant_value}')
        print(f'       CSV file (menu items): {crawled_restaurant["csv_file_menu"]}')
        print(f'       CSV file (items modifiers): {crawled_restaurant["csv_file_modifiers"]}')


def display_elapsed_time(start_time):
    print()
    elapsed_time = datetime.now() - start_time
    print(f'Elapsed time: {elapsed_time}')
