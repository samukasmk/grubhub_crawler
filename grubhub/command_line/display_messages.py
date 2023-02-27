import traceback
from datetime import datetime
from grubhub.output.csv.export_fields import csv_field_names

def display_program_title():
    print()
    print('[GrubHub Restaurant Crawler]')


def display_horizontal_rule():
    print('-' * 160)


def display_crawl_mode(is_collecting_all_information, csv_folder):
    if is_collecting_all_information:
        crawl_mode = 'MANY INFORMATION AS POSSIBLE'
        menu_items_fields = ', '.join(csv_field_names['menu_items']['all_fields'])
        items_modifiers_fields = ', '.join(csv_field_names['items_modifiers']['all_fields'])
    else:
        crawl_mode = 'BASIC INFORMATION'
        menu_items_fields = ', '.join(csv_field_names['menu_items']['basic_fields'])
        items_modifiers_fields = ', '.join(csv_field_names['items_modifiers']['basic_fields'])

    print()
    print(f'Crawling mode: [{crawl_mode}]')
    display_horizontal_rule()
    print(f'       Created folder to write the CSV files: {csv_folder}')
    print(f'       CSV fields for file of (menu items): {menu_items_fields}')
    print(f'       CSV fields for file of (items modifiers): {items_modifiers_fields}')


def display_getting_title():
    print()
    print('Getting restaurants data:')


def display_restaurants_info(crawled_restaurants):
    for crawled_restaurant in crawled_restaurants:
        display_horizontal_rule()
        print(f'-> ({crawled_restaurant.async_index}) Restaurant URL: {crawled_restaurant.restaurant_url}')

        if crawled_restaurant.success:
            print(f'       Crawler state: success')
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
