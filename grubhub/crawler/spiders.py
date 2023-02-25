import asyncio
from typing import Optional, Dict
from dataclasses import dataclass
from grubhub.api.api import GrubHubAPI
from grubhub.crawler.extractors import DataExtractor
from grubhub.crawler.output_managers import OutputManager
from grubhub.crawler.formaters import get_restaurant_id_from_url


@dataclass
class CrawlerResponse:
    success: Optional[bool] = None
    failure_moment: Optional[str] = None
    failure_exception: Optional[Exception] = None
    async_index: Optional[int] = None
    restaurant_url: Optional[str] = None
    restaurant_info: Optional[Dict] = None
    csv_file_menu: Optional[str] = None
    csv_file_modifiers: Optional[str] = None


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
        try:
            restaurant_data = await grubhub_api.get_restaurant_data(restaurant_id)
        except Exception as exc:
            return CrawlerResponse(success=False,
                                   failure_moment='get_restaurant_data',
                                   failure_exception=exc,
                                   async_index=self.async_index,
                                   restaurant_url=self.restaurant_url)

        # extract basic restaurant information
        try:
            restaurant_info = self.data_extractor.extract_restaurant_info(restaurant_data)
        except Exception as exc:
            return CrawlerResponse(success=False,
                                   failure_moment='extract_restaurant_info',
                                   failure_exception=exc,
                                   async_index=self.async_index,
                                   restaurant_url=self.restaurant_url)

        # extract menu items information
        try:
            menu_items, items_id = self.data_extractor.extract_menu_items(restaurant_data)
        except Exception as exc:
            return CrawlerResponse(success=False,
                                   failure_moment='extract_menu_items',
                                   failure_exception=exc,
                                   async_index=self.async_index,
                                   restaurant_url=self.restaurant_url)

        # write csv file for menu items
        try:
            csv_file_menu = await self.output_manager.write_csv_menu_items(menu_items)
        except Exception as exc:
            return CrawlerResponse(success=False,
                                   failure_moment='write_csv_menu_items',
                                   failure_exception=exc,
                                   async_index=self.async_index,
                                   restaurant_url=self.restaurant_url)

        # for each menu item: get the item modifiers
        try:
            menu_items_data = await asyncio.gather(
                *[grubhub_api.get_menu_item_data(restaurant_id, item_id)
                  for item_id in items_id])
        except Exception as exc:
            return CrawlerResponse(success=False,
                                   failure_moment='get_menu_item_data',
                                   failure_exception=exc,
                                   async_index=self.async_index,
                                   restaurant_url=self.restaurant_url)

        # extract item modifiers information
        try:
            menu_modifiers = []
            for menu_item_data in menu_items_data:
                menu_modifiers += self.data_extractor.extract_menu_modifiers(menu_item_data)
        except Exception as exc:
            return CrawlerResponse(success=False,
                                   failure_moment='extract_menu_modifiers',
                                   failure_exception=exc,
                                   async_index=self.async_index,
                                   restaurant_url=self.restaurant_url)

        # write csv file for items modifiers
        try:
            csv_file_modifiers = await self.output_manager.write_csv_menu_modifiers(menu_modifiers)
        except Exception as exc:
            return CrawlerResponse(success=False,
                                   failure_moment='write_csv_menu_modifiers',
                                   failure_exception=exc,
                                   async_index=self.async_index,
                                   restaurant_url=self.restaurant_url)

        # return crawled info
        return CrawlerResponse(success=True,
                               async_index=self.async_index,
                               restaurant_url=self.restaurant_url,
                               restaurant_info=restaurant_info,
                               csv_file_menu=csv_file_menu,
                               csv_file_modifiers=csv_file_modifiers)
