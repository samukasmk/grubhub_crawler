import traceback
from datetime import datetime


def display_title():
    print()
    print('[GrubHub Restaurant Crawler]')
    print()
    print('Getting restaurants data:')


def display_horizontal_rule():
    print('-' * 160)


def display_restaurants_info(crawled_restaurants):
    for crawled_restaurant in crawled_restaurants:
        display_horizontal_rule()
        print(f'-> ({crawled_restaurant.async_index}) Restaurant URL: {crawled_restaurant.restaurant_url}')

        if crawled_restaurant.success:
            print(f'       Crawler state: succes')
            for restaurant_key, restaurant_value in crawled_restaurant.restaurant_info.items():
                print(f'       {restaurant_key}: {restaurant_value}')
            print(f'       CSV file (menu items): {crawled_restaurant.csv_file_menu}')
            print(f'       CSV file (items modifiers): {crawled_restaurant.csv_file_modifiers}')

        else:


            print(f'       Crawler state: failed')
            print(f'       Failure moment: {crawled_restaurant.failure_moment}')
            print(f'       Failure reason: {str(crawled_restaurant.failure_exception)}')
            failure_traceback = "".join(traceback.format_exception(crawled_restaurant.failure_exception))
            print(f'       Failure traceback:')
            print(failure_traceback)


def display_elapsed_time(start_time):
    print()
    elapsed_time = datetime.now() - start_time
    print(f'Elapsed time: {elapsed_time}')
