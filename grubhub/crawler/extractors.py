from grubhub.crawler.formaters import normalize_price_value


class DataExtractor():
    def __init__(self, verbose_csv=False):
        self.verbose_csv = verbose_csv

    def extract_restaurant_info(self, restaurant_data):
        return {"Restaurant Name": restaurant_data['restaurant']['name'],
                "Restaurant Address": restaurant_data['restaurant']['address']['street_address'],
                "Restaurant City": restaurant_data['restaurant']['address']['locality'],
                "Restaurant State": restaurant_data['restaurant']['address']['region'],
                "Restaurant Stars": restaurant_data['restaurant']['rating']['rating_value'],
                "Restaurant Review Count": restaurant_data['restaurant']['rating']['rating_count']}

    def extract_menu_items(self, restaurant_data):
        menu_items = []
        items_id = []
        for menu_category in restaurant_data['restaurant']['menu_category_list']:
            for menu_item in menu_category['menu_item_list']:
                # save to write on csv
                extra_fields = {'Item ID': menu_item['id']} if self.verbose_csv else {}
                menu_items.append({'Category Name': menu_category['name'],
                                   'Item Name': menu_item['name'],
                                   'Item Description': menu_item['description'],
                                   'Item Price': normalize_price_value(menu_item['price']['amount']),
                                   **extra_fields})
                items_id.append(menu_item['id'])
        return menu_items, items_id

    def extract_menu_modifiers(self, menu_item_data):
        menu_modifiers = []
        for choice_category_list in menu_item_data['choice_category_list']:
            for choice_option_list in choice_category_list['choice_option_list']:
                options_amount = len(choice_category_list['choice_option_list'])
                extra_fields = {'Item ID': menu_item_data['id'],
                                'Item Name': menu_item_data['name']} if self.verbose_csv else {}
                menu_modifiers.append({'Modifier Group Name': choice_category_list['name'],
                                       'Modifier Min': choice_category_list['min_choice_options'],
                                       'Modifier Max': choice_category_list.get('max_choice_options', options_amount),
                                       'Option Name': choice_option_list['description'],
                                       'Option Price': normalize_price_value(choice_option_list['price']['amount']),
                                       **extra_fields})
        return menu_modifiers
