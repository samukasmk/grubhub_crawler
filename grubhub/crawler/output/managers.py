import re
import csv
import aiofiles
import aiofiles.os
from aiocsv import AsyncDictWriter


class OutputManager():
    def __init__(self, restaurant_url, csv_folder='./output_csv', collect_all_information=False, async_index=None):
        self.restaurant_url = restaurant_url
        self.collect_all_information = collect_all_information
        self.async_number = async_index
        self.regex = {'file_name': re.compile('[^a-zA-Z0-9\.]')}
        self.csv_folder = csv_folder

    def __define_csv_file_path(self, prefix_name):
        normalized_name = self.regex['file_name'].sub('_', self.restaurant_url)
        return f'{self.csv_folder}/{prefix_name}_{normalized_name}.csv'

    async def __create_empty_csv_file(self, file_path, field_names):
        async with aiofiles.open(file_path, mode="w", encoding="utf-8", newline="") as afp:
            writer = AsyncDictWriter(afp, fieldnames=field_names, restval="NULL", quoting=csv.QUOTE_ALL)
            await writer.writeheader()

    async def __append_csv_lines(self, file_path, field_names, lines_dict_list):
        async with aiofiles.open(file_path, mode="a", encoding="utf-8", newline="") as afp:
            writer = AsyncDictWriter(afp, fieldnames=field_names, restval="NULL", quoting=csv.QUOTE_ALL)
            await writer.writerows(lines_dict_list)

    async def write_csv_menu_items(self, menu_items):
        file_path = self.__define_csv_file_path('menu_downloads')
        field_names = ['Category Name', 'Item Name', 'Item Description', 'Item Price']
        if self.collect_all_information:
            field_names = ['Category ID', 'Category Name', 'Category Is Available',
                           'Item ID', 'Item Name', 'Item Description', 'Item Is Available', 'Item Is Popular',
                           'Item Price', 'Item Price Currency',
                           'Item Delivery Price', 'Item Delivery Price Currency',
                           'Item Pickup Price', 'Item Pickup Price Currency',
                           'Item Tax Rate', 'Item Tax Name', 'Item Tax Is Included in Item Price',
                           'Category Sequence', 'Item Sequence']
        await self.__create_empty_csv_file(file_path, field_names)
        await self.__append_csv_lines(file_path, field_names, menu_items)
        return file_path

    async def write_csv_menu_modifiers(self, menu_modifiers):
        file_path = self.__define_csv_file_path('modifier_downloads')
        field_names = ['Modifier Group Name', 'Modifier Min', 'Modifier Max', 'Option Name', 'Option Price']
        if self.collect_all_information:
            field_names = ['Item ID', 'Item Name', 'Modifier Group Name', 'Option Name',
                           'Option Price', 'Option Price Currency',
                           'Option Delivery Price', 'Option Delivery Price Currency',
                           'Option Pickup Price', 'Option Pickup Price Currency',
                           'Modifier Min', 'Modifier Max', 'Modifier Sequence Number',
                           'Modifier Is Available', 'Modifier ID', 'Modifier Group Display Type']
        await self.__create_empty_csv_file(file_path, field_names)
        await self.__append_csv_lines(file_path, field_names, menu_modifiers)
        return file_path
