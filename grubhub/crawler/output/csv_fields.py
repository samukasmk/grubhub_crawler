csv_field_names = {
    # Define the order of field names for CSV file of menu items
    'menu_items': {
        'basic_fields': ['Category Name', 'Item Name', 'Item Description', 'Item Price'],
        'all_fields': ['Category ID', 'Category Name', 'Category Is Available',
                       'Item ID', 'Item Name', 'Item Description', 'Item Is Available', 'Item Is Popular',
                       'Item Price', 'Item Price Currency',
                       'Item Delivery Price', 'Item Delivery Price Currency',
                       'Item Pickup Price', 'Item Pickup Price Currency',
                       'Item Tax Rate', 'Item Tax Name', 'Item Tax Is Included in Item Price',
                       'Category Sequence', 'Item Sequence'],
    },

    # Define the order of field names for CSV file of items modifiers
    'items_modifiers': {
        'basic_fields': ['Modifier Group Name', 'Modifier Min', 'Modifier Max', 'Option Name', 'Option Price'],
        'all_fields': ['Item ID', 'Item Name', 'Modifier Group Name', 'Option Name',
                       'Option Price', 'Option Price Currency',
                       'Option Delivery Price', 'Option Delivery Price Currency',
                       'Option Pickup Price', 'Option Pickup Price Currency',
                       'Modifier Min', 'Modifier Max', 'Modifier Sequence Number',
                       'Modifier Is Available', 'Modifier ID', 'Modifier Group Display Type']
    }
}
