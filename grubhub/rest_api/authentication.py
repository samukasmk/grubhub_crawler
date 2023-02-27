import re
import aiohttp
from lxml import html


class GrubHubOAuthClientID:
    def __init__(self):
        self.client_id = None
        self.regex = {'api_url': re.compile("apiUrl:[ \n]*['\"]http[s]\:\/\/(api-gtm.grubhub.com)[\/]*['\"]"),
                      'client_id': re.compile("clientId:[ \n]*['\"](.*)['\"]")}
        self.javascript_block_xpath = '//script[@type="text/javascript"]'

    async def __get_static_webpage(self):
        website_static_url = 'https://www.grubhub.com/eat/static-content-unauth?contentOnly=1'
        async with aiohttp.ClientSession() as session:
            async with session.get(website_static_url, raise_for_status=True) as response:
                return await response.text()

    def __extract_client_id(self, html_webpage):
        found_client_id = []
        html_tree = html.fromstring(html_webpage)
        # sweep the html tree searching a javascript block with clientId
        for javascript_block in html_tree.xpath(self.javascript_block_xpath):
            if self.regex['api_url'].findall(javascript_block.text):
                found_client_id += self.regex['client_id'].findall(javascript_block.text)
        if found_client_id:
            return found_client_id[0]

    async def get_client_id(self):
        html_webpage = await self.__get_static_webpage()
        return self.__extract_client_id(html_webpage)
