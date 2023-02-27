from datetime import datetime

import uvloop
import asyncio

from grubhub.command_line.display_messages import (display_program_title, display_horizontal_rule,
                                                   display_crawl_mode, display_getting_title,
                                                   display_restaurants_info, display_elapsed_time)
from grubhub.command_line.argument_parser import parse_command_line_arguments
from grubhub.rest_api.authentication import GrubHubOAuthClientID
from grubhub.crawler.restaurants import GrubhubRestaurantSpider
from grubhub.output.csv.managers import CsvOutputManager


async def main():
    # parse command line arguments and get restaurants id
    args = parse_command_line_arguments()

    # display program title
    display_program_title()

    # create csv folder if it not exists
    csv_folder = './output_csv'
    display_crawl_mode(args.collect_all_information, csv_folder)
    await CsvOutputManager.ensure_csv_folder_exists(csv_folder)

    # display getting restaurants title
    display_getting_title()

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
            collect_all_information=args.collect_all_information,
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
