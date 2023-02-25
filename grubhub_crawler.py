from datetime import datetime

import uvloop
import asyncio

from grubhub.command_line.display_messages import (display_title, display_horizontal_rule,
                                                   display_restaurants_info, display_elapsed_time)
from grubhub.command_line.argument_parser import parse_command_line_arguments
from grubhub.command_line.csv_folder import ensure_csv_folder_exists

from grubhub.api.authentication import GrubHubOAuthClientID
from grubhub.crawler.spiders import GrubhubRestaurantSpider


async def main():
    # parse command line arguments and get restaurants id
    args = parse_command_line_arguments()

    # display program title
    display_title()

    # create csv folder if it not exists
    csv_folder = './output_csv'
    await ensure_csv_folder_exists(csv_folder)

    # measure time from begin
    start_time = datetime.now()

    # get client id to authenticate on API
    client_id = await GrubHubOAuthClientID().get_client_id()

    # for each restaurant_url crawl the data
    crawled_restaurants = await asyncio.gather(
        *[GrubhubRestaurantSpider(
            restaurant_url=restaurant_url,
            client_id=client_id,
            csv_folder=csv_folder,
            verbose_csv=args.verbose_csv,
            async_index=call_index + 1
        ).crawl_data()
          for call_index, restaurant_url in enumerate(args.urls)])

    # display information
    display_restaurants_info(crawled_restaurants)
    display_horizontal_rule()
    display_elapsed_time(start_time)


if __name__ == '__main__':
    # speeds up with faster uvloop asyncio runner
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    # create asyncio loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
