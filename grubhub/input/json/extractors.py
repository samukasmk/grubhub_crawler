from grubhub.input.formaters import normalize_price_value


class JsonDataExtractor():
    def __init__(self, collect_all_information=False):
        self.collect_all_information = collect_all_information

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
            for menu_item_data in menu_category['menu_item_list']:
                # save to write on csv
                fields = {'Category Name': menu_category['name'],
                          'Item Name': menu_item_data['name'],
                          'Item Description': menu_item_data['description'],
                          'Item Price': normalize_price_value(menu_item_data['price']['amount'])}
                if self.collect_all_information:
                    fields.update(
                        {'Category ID': menu_category['id'],
                         'Category Is Available': menu_category['available'],
                         'Category Sequence': menu_category['sequence'],
                         'Item Is Available': menu_item_data['available'],
                         'Item Is Popular': menu_item_data['popular'],
                         'Item Price Currency': menu_item_data['price']['currency'],
                         'Item Delivery Price': normalize_price_value(menu_item_data['delivery_price']['amount']),
                         'Item Delivery Price Currency': menu_item_data['delivery_price']['currency'],
                         'Item Pickup Price': normalize_price_value(menu_item_data['pickup_price']['amount']),
                         'Item Pickup Price Currency': menu_item_data['pickup_price']['currency'],
                         'Item Tax Rate': menu_item_data['tax_rate']['rate'],
                         'Item Tax Name': menu_item_data['tax_rate']['name'],
                         'Item Tax Is Included in Item Price': menu_item_data['tax_rate']['included_in_item_price'],
                         'Item ID': menu_item_data['id'],
                         'Item Sequence': menu_item_data['sequence']})
                menu_items.append(fields)
                items_id.append(menu_item_data['id'])
        return menu_items, items_id

    def extract_menu_modifiers(self, menu_item_data):
        menu_modifiers = []
        for choice_category_list in menu_item_data['choice_category_list']:
            for choice_option_list in choice_category_list['choice_option_list']:
                options_amount = len(choice_category_list['choice_option_list'])
                fields = {'Modifier Group Name': choice_category_list['name'],
                          'Modifier Min': choice_category_list['min_choice_options'],
                          'Modifier Max': choice_category_list.get('max_choice_options', options_amount),
                          'Option Name': choice_option_list['description'],
                          'Option Price': normalize_price_value(choice_option_list['price']['amount'])}
                if self.collect_all_information:
                    fields.update(
                        {'Item ID': menu_item_data['id'],
                         'Item Name': menu_item_data['name'],
                         'Modifier Sequence Number': choice_option_list['sequence'],
                         'Modifier Is Available': choice_option_list['available'],
                         'Modifier ID': choice_option_list['id'],
                         'Modifier Group Display Type': choice_category_list.get(
                             'display_settings', {}).get('display_type', 'CHOOSE_SINGLE_OPTIONAL'),
                         'Option Price Currency': choice_option_list['price']['currency'],
                         'Option Delivery Price': normalize_price_value(choice_option_list['delivery_price']['amount']),
                         'Option Delivery Price Currency': choice_option_list['delivery_price']['currency'],
                         'Option Pickup Price': normalize_price_value(choice_option_list['pickup_price']['amount']),
                         'Option Pickup Price Currency': choice_option_list['pickup_price']['currency']})
                menu_modifiers.append(fields)
        return menu_modifiers
