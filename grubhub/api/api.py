import aiohttp


class GrubHubAPI:
    def __init__(self, client_id):
        self.client_id = client_id
        self.auth_token = None
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        self.session.headers.update(self.__headers())
        # authenticate if not already done
        if not self.auth_token:
            await self.__get_auth_token()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    def __headers(self):
        return {'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                               '(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'),
                'authorization': 'Bearer' + f' {self.auth_token}' if self.auth_token else '',
                'content-type': 'application/json;charset=UTF-8'}

    async def __get_auth_token(self):
        auth_url = 'https://api-gtm.grubhub.com/auth'
        auth_parameters = '{"client_id":"' + self.client_id + '","scope":"anonymous","device_id":1234567890,"brand":"GRUBHUB"}'
        async with self.session.post(auth_url, data=auth_parameters) as response:
            response_json = await response.json()
            self.auth_token = response_json['session_handle']['access_token']
        # update session headers with new access token
        self.session.headers.update(self.__headers())

    async def get_restaurant_data(self, restaurant_id):
        restaurant_api_url = f'https://api-gtm.grubhub.com/restaurants/{restaurant_id}'
        async with self.session.get(restaurant_api_url) as response:
            return await response.json()

    async def get_menu_item_data(self, restaurant_id, item_id):
        menu_items_url = f"https://api-gtm.grubhub.com/restaurants/{restaurant_id}/menu_items/{item_id}"
        async with self.session.get(menu_items_url) as response:
            return await response.json()
