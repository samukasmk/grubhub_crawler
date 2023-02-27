import re
import csv
import aiofiles
import aiofiles.os
from aiocsv import AsyncDictWriter

from grubhub.output.csv.export_fields import csv_field_names


class CsvOutputManager():
    def __init__(self, restaurant_url, csv_folder='./output_csv', collect_all_information=False, async_index=None):
        self.restaurant_url = restaurant_url
        self.collect_all_information = collect_all_information
        self.async_number = async_index
        self.regex = {'file_name': re.compile('[^a-zA-Z0-9\.]')}
        self.csv_folder = csv_folder

    @classmethod
    async def ensure_csv_folder_exists(cls, csv_folder):
        if await aiofiles.os.path.exists(csv_folder) is False:
            await aiofiles.os.makedirs(csv_folder)

    def __define_csv_file_path(self, prefix_name):
        full_type = '_full' if self.collect_all_information else ''
        normalized_name = self.regex['file_name'].sub('_', self.restaurant_url)
        return f'{self.csv_folder}/{prefix_name}{full_type}_downloads_{normalized_name}.csv'

    async def __create_empty_csv_file(self, file_path, field_names):
        async with aiofiles.open(file_path, mode="w", encoding="utf-8", newline="") as afp:
            writer = AsyncDictWriter(afp, fieldnames=field_names, restval="NULL", quoting=csv.QUOTE_ALL)
            await writer.writeheader()

    async def __append_csv_lines(self, file_path, field_names, lines_dict_list):
        async with aiofiles.open(file_path, mode="a", encoding="utf-8", newline="") as afp:
            writer = AsyncDictWriter(afp, fieldnames=field_names, restval="NULL", quoting=csv.QUOTE_ALL)
            await writer.writerows(lines_dict_list)

    async def write_csv_menu_items(self, menu_items):
        file_path = self.__define_csv_file_path('menu')
        fields_type = 'all_fields' if self.collect_all_information else 'basic_fields'
        await self.__create_empty_csv_file(file_path, csv_field_names['menu_items'][fields_type])
        await self.__append_csv_lines(file_path, csv_field_names['menu_items'][fields_type], menu_items)
        return file_path

    async def write_csv_menu_modifiers(self, menu_modifiers):
        file_path = self.__define_csv_file_path('modifiers')
        fields_type = 'all_fields' if self.collect_all_information else 'basic_fields'
        await self.__create_empty_csv_file(file_path, csv_field_names['items_modifiers'][fields_type])
        await self.__append_csv_lines(file_path, csv_field_names['items_modifiers'][fields_type], menu_modifiers)
        return file_path
