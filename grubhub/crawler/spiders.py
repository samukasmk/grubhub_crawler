import asyncio
from grubhub.api.api import GrubHubAPI
from grubhub.crawler.extractors import DataExtractor
from grubhub.crawler.output_managers import OutputManager
from grubhub.crawler.formaters import get_restaurant_id_from_url


class GrubhubRestaurantSpider():
    def __init__(self, restaurant_url, client_id, csv_folder='./output_csv', verbose_csv=False, async_index=None):
        self.restaurant_url = restaurant_url
        self.client_id = client_id
        self.async_index = async_index
        self.data_extractor = DataExtractor(verbose_csv)
        self.output_manager = OutputManager(restaurant_url, csv_folder, verbose_csv, self.async_index)

    async def crawl_data(self):
        async with GrubHubAPI(self.client_id) as grubhub_api:
            return await self.__crawl_restaurant(grubhub_api)

    async def __crawl_restaurant(self, grubhub_api):
        # get restaurant info
        restaurant_id = get_restaurant_id_from_url(self.restaurant_url)
        restaurant_data = await grubhub_api.get_restaurant_data(restaurant_id)  # await

        # extract needed information
        restaurant_info = self.data_extractor.extract_restaurant_info(restaurant_data)
        menu_items, items_id = self.data_extractor.extract_menu_items(restaurant_data)

        # write csv file for menu downloads
        csv_file_menu = await self.output_manager.write_csv_menu_items(menu_items)

        menu_items_data = await asyncio.gather(
            *[grubhub_api.get_menu_item_data(restaurant_id, item_id)
              for item_id in items_id])

        menu_modifiers = []
        for menu_item_data in menu_items_data:
            menu_modifiers += self.data_extractor.extract_menu_modifiers(menu_item_data)

        # write csv file for menu downloads
        csv_file_modifiers = await self.output_manager.write_csv_menu_modifiers(menu_modifiers)

        # return crawled info
        return {"async_index": self.async_index,
                "restaurant_url": self.restaurant_url,
                "restaurant_info": restaurant_info,
                "csv_file_menu": csv_file_menu,
                "csv_file_modifiers": csv_file_modifiers}
