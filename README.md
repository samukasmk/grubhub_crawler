# grubhub_crawler
A Crawler for grab Restaurants information from GrubHub platform

# Installation
### Requirements
This project runs on top of (Python 3.11.2)

### To local installation
```sh
# download the project files
git clone https://github.com/samukasmk/grubhub_crawler.git

# create and activate a virtualenv
python3 -m venv ./venv
source ./venv/bin/activate

# install the requirements
pip install -r requirements.txt
```

# Collecting the data
There is 2 types of data collections:

**Simple data collection:** collect just basic information such as:
 - (from restaurant): restaurant name, address, city, state, stars, review count
 - (from menu items): category name, item name, item description, item price
 - (from modifiers items): modifier group name, modifier min, modifier max, option name, option price

**Full data collection:** collects much information as possible as too *using command line argument* `--collect-all-information`:
 - (from menu items): category or item is available, item is popularity, item price for delivery or pickup, tax rate, ...
 - (from modifiers items): modifier availability, option price for delivery or pickup, ...



## Executing the Simple data collection
This is the default option when you execute de command line, follow an example of command line execution for a **Simple data collection**:
```bash
$ python grubhub_crawler.py \
  --urls https://www.grubhub.com/restaurant/dosa-love-893-e-el-camino-real-sunnyvale/3024935 \
         https://www.grubhub.com/restaurant/beaus-breakfast-burritos-1404-madison-ave-new-york/3235140 \
         https://www.grubhub.com/restaurant/impeckable-wings-901-nw-24th-st-san-antonio/3159434 \
         https://www.grubhub.com/restaurant/the-vegan-grill-5155-3rd-st-san-francisco/2994242
```
Follow the sample of output for the **Simple data collection**:
```
[GrubHub Restaurant Crawler]

Crawling mode: [BASIC INFORMATION]
----------------------------------------------------------------------------------------------------------------------------------------------------------------
       Created folder to write the CSV files ./output_csv
       CSV fields for file of (menu items): Category Name, Item Name, Item Description, Item Price
       CSV fields for file of (items modifiers): Modifier Group Name, Modifier Min, Modifier Max, Option Name, Option Price

Getting restaurants data:
----------------------------------------------------------------------------------------------------------------------------------------------------------------
-> (1) Restaurant URL: https://www.grubhub.com/restaurant/dosa-love-893-e-el-camino-real-sunnyvale/3024935
       Crawler state: success
       Restaurant Name: Dosa Love
       Restaurant Address: 893 E El Camino Real
       Restaurant City: Sunnyvale
       Restaurant State: CA
       Restaurant Stars: 4
       Restaurant Review Count: 13
       CSV file (menu items): ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_dosa_love_893_e_el_camino_real_sunnyvale_3024935.csv
       CSV file (items modifiers): ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_dosa_love_893_e_el_camino_real_sunnyvale_3024935.csv
----------------------------------------------------------------------------------------------------------------------------------------------------------------
-> (2) Restaurant URL: https://www.grubhub.com/restaurant/beaus-breakfast-burritos-1404-madison-ave-new-york/3235140
       Crawler state: success
       Restaurant Name: Beau's Breakfast Burritos
       Restaurant Address: 1404 Madison Ave
       Restaurant City: New York
       Restaurant State: NY
       Restaurant Stars: 3
       Restaurant Review Count: 1
       CSV file (menu items): ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_beaus_breakfast_burritos_1404_madison_ave_new_york_3235140.csv
       CSV file (items modifiers): ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_beaus_breakfast_burritos_1404_madison_ave_new_york_3235140.csv
----------------------------------------------------------------------------------------------------------------------------------------------------------------
-> (3) Restaurant URL: https://www.grubhub.com/restaurant/impeckable-wings-901-nw-24th-st-san-antonio/3159434
       Crawler state: success
       Restaurant Name: Impeckable Wings
       Restaurant Address: 901 NW 24th St
       Restaurant City: San Antonio
       Restaurant State: TX
       Restaurant Stars: 3
       Restaurant Review Count: 1
       CSV file (menu items): ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_impeckable_wings_901_nw_24th_st_san_antonio_3159434.csv
       CSV file (items modifiers): ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_impeckable_wings_901_nw_24th_st_san_antonio_3159434.csv
----------------------------------------------------------------------------------------------------------------------------------------------------------------
-> (4) Restaurant URL: https://www.grubhub.com/restaurant/the-vegan-grill-5155-3rd-st-san-francisco/2994242
       Crawler state: success
       Restaurant Name: The Vegan Grill
       Restaurant Address: 5155 3rd St
       Restaurant City: San Francisco
       Restaurant State: CA
       Restaurant Stars: 3
       Restaurant Review Count: 10
       CSV file (menu items): ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_the_vegan_grill_5155_3rd_st_san_francisco_2994242.csv
       CSV file (items modifiers): ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_the_vegan_grill_5155_3rd_st_san_francisco_2994242.csv
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Elapsed time: 0:00:02.943267
```

## Executing the Full data collection
To execute the full data collection you need to pass the argument `--collect-all-information`, Below there is a example:
```bash
$ python grubhub_crawler.py \
  --collect-all-information \
  --urls https://www.grubhub.com/restaurant/dosa-love-893-e-el-camino-real-sunnyvale/3024935 \
         https://www.grubhub.com/restaurant/beaus-breakfast-burritos-1404-madison-ave-new-york/3235140 \
         https://www.grubhub.com/restaurant/impeckable-wings-901-nw-24th-st-san-antonio/3159434 \
         https://www.grubhub.com/restaurant/the-vegan-grill-5155-3rd-st-san-francisco/2994242
```
Follow the sample of output for the **Simple data collection**:
```
[GrubHub Restaurant Crawler]

Crawling mode: [MANY INFORMATION AS POSSIBLE]
----------------------------------------------------------------------------------------------------------------------------------------------------------------
       Created folder to write the CSV files: ./output_csv
       CSV fields for file of (menu items): Category ID, Category Name, Category Is Available, Item ID, Item Name, Item Description, Item Is Available, Item Is Popular, Item Price, Item Price Currency, Item Delivery Price, Item Delivery Price Currency, Item Pickup Price, Item Pickup Price Currency, Item Tax Rate, Item Tax Name, Item Tax Is Included in Item Price, Category Sequence, Item Sequence
       CSV fields for file of (items modifiers): Item ID, Item Name, Modifier Group Name, Option Name, Option Price, Option Price Currency, Option Delivery Price, Option Delivery Price Currency, Option Pickup Price, Option Pickup Price Currency, Modifier Min, Modifier Max, Modifier Sequence Number, Modifier Is Available, Modifier ID, Modifier Group Display Type

Getting restaurants data:
----------------------------------------------------------------------------------------------------------------------------------------------------------------
-> (1) Restaurant URL: https://www.grubhub.com/restaurant/dosa-love-893-e-el-camino-real-sunnyvale/3024935
       Crawler state: success
       Restaurant Name: Dosa Love
       Restaurant Address: 893 E El Camino Real
       Restaurant City: Sunnyvale
       Restaurant State: CA
       Restaurant Stars: 4
       Restaurant Review Count: 13
       CSV file (menu items): ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_dosa_love_893_e_el_camino_real_sunnyvale_3024935.csv
       CSV file (items modifiers): ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_dosa_love_893_e_el_camino_real_sunnyvale_3024935.csv
----------------------------------------------------------------------------------------------------------------------------------------------------------------
-> (2) Restaurant URL: https://www.grubhub.com/restaurant/beaus-breakfast-burritos-1404-madison-ave-new-york/3235140
       Crawler state: success
       Restaurant Name: Beau's Breakfast Burritos
       Restaurant Address: 1404 Madison Ave
       Restaurant City: New York
       Restaurant State: NY
       Restaurant Stars: 3
       Restaurant Review Count: 1
       CSV file (menu items): ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_beaus_breakfast_burritos_1404_madison_ave_new_york_3235140.csv
       CSV file (items modifiers): ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_beaus_breakfast_burritos_1404_madison_ave_new_york_3235140.csv
----------------------------------------------------------------------------------------------------------------------------------------------------------------
-> (3) Restaurant URL: https://www.grubhub.com/restaurant/impeckable-wings-901-nw-24th-st-san-antonio/3159434
       Crawler state: success
       Restaurant Name: Impeckable Wings
       Restaurant Address: 901 NW 24th St
       Restaurant City: San Antonio
       Restaurant State: TX
       Restaurant Stars: 3
       Restaurant Review Count: 1
       CSV file (menu items): ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_impeckable_wings_901_nw_24th_st_san_antonio_3159434.csv
       CSV file (items modifiers): ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_impeckable_wings_901_nw_24th_st_san_antonio_3159434.csv
----------------------------------------------------------------------------------------------------------------------------------------------------------------
-> (4) Restaurant URL: https://www.grubhub.com/restaurant/the-vegan-grill-5155-3rd-st-san-francisco/2994242
       Crawler state: success
       Restaurant Name: The Vegan Grill
       Restaurant Address: 5155 3rd St
       Restaurant City: San Francisco
       Restaurant State: CA
       Restaurant Stars: 3
       Restaurant Review Count: 10
       CSV file (menu items): ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_the_vegan_grill_5155_3rd_st_san_francisco_2994242.csv
       CSV file (items modifiers): ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_the_vegan_grill_5155_3rd_st_san_francisco_2994242.csv
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Elapsed time: 0:00:03.960370
```

## Output files to CSV format
Any CSV file is stored in folder `./output_csv`.
The CSV fields can have more fields if activated the **Full data collection** with argument `--collect-all-information`

### CSV file (Full data collection: of menu items):
> **File path:** ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_the_vegan_grill_5155_3rd_st_san_francisco_2994242.csv

| **"Category Name"** | **"Item Name"**                 | **"Item Description"**                                                          | **"Item Price"** |
|---------------------|---------------------------------|---------------------------------------------------------------------------------|------------------|
| "Viva Vegan Pizza " | "Margherita Of Savory Pizza"    | "Vegan cheese, fresh tomato sauce, basil, baked on a hand-tossed dough "        | "0.0"            |
| "Viva Vegan Pizza " | "Viva La Vegan Cheese Pizza"    | "Fresh tomato sauce, shredded vegan cheese baked on a hand-tossed dough"        | "0.0"            |
| "Viva Vegan Pizza " | "Lusty Love Loaded Vegan Pizza" | "Fresh mushrooms, green peppers, and vegan cheese baked on a hand-tossed dough" | "0.0"            |


### CSV file (Full data collection: of menu items):
> **File path:** ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_the_vegan_grill_5155_3rd_st_san_francisco_2994242.csv

| **"Modifier Group Name"** | **"Modifier Min"** | **"Modifier Max"** | **"Option Name"** | **"Option Price"** |
|---------------------------|--------------------|--------------------|-------------------|--------------------|
| "Choose Your Size"        | "1"                | "1"                | "Small"           | "18.35"            |
| "Choose Your Size"        | "1"                | "1"                | "Medium"          | "20.35"            |
| "Choose Your Size"        | "1"                | "1"                | "Large"           | "23.35"            |


### CSV file (Full data collection: of menu items):
> **File path:** ./output_csv/modifier_full_downloads_https___www.grubhub.com_restaurant_beaus_breakfast_burritos_1404_madison_ave_new_york_3235140.csv

| **"Category ID"** | **"Category Name"**              | **"Category Is Available"** | **"Item ID"** | **"Item Name"**                     | **"Item Description"**                                                                                     | **"Item Is Available"** | **"Item Is Popular"** | **"Item Price"** | **"Item Price Currency"** | **"Item Delivery Price"** | **"Item Delivery Price Currency"** | **"Item Pickup Price"** | **"Item Pickup Price Currency"** | **"Item Tax Rate"** | **"Item Tax Name"** | **"Item Tax Is Included in Item Price"** | **"Category Sequence"** | **"Item Sequence"** |
|-------------------|----------------------------------|-----------------------------|---------------|-------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------|------------------|---------------------------|---------------------------|------------------------------------|-------------------------|----------------------------------|---------------------|---------------------|------------------------------------------|-------------------------|---------------------|
| "889971135"       | "Breaking Bad Breakfast Burrito" | "True"                      | "13828721776" | "No Fuss No Muss Breakfast Burrito" | "Eggs, cheddar cheese, onions, tomatoes wrapped in a flour tortilla."                                      | "True"                  | "False"               | "10.99"          | "USD"                     | "10.99"                   | "USD"                              | "10.99"                 | "USD"                            | "8.875"             | "RestaurantTax"     | "False"                                  | "1"                     | "1"                 |
| "889971135"       | "Breaking Bad Breakfast Burrito" | "True"                      | "13833891837" | "The Feisty Burrito"                | "Eggs, spicy jalapenos, hot sauce, cheddar cheese, onions, tomatoes wrapped in a flour tortilla."          | "True"                  | "False"               | "10.99"          | "USD"                     | "10.99"                   | "USD"                              | "10.99"                 | "USD"                            | "8.875"             | "RestaurantTax"     | "False"                                  | "1"                     | "2"                 |
| "889971135"       | "Breaking Bad Breakfast Burrito" | "True"                      | "13825959643" | "Chorizo Baby Breakfast"            | "Chorizo, eggs, spicy jalapenos, hot sauce, cheddar cheese, onions, tomatoes wrapped in a flour tortilla." | "True"                  | "False"               | "10.99"          | "USD"                     | "10.99"                   | "USD"                              | "10.99"                 | "USD"                            | "8.875"             | "RestaurantTax"     | "False"                                  | "1"                     | "3"                 |

### CSV file (Full data collection: of menu items):
> **File path:** ./output_csv/modifier_full_downloads_https___www.grubhub.com_restaurant_beaus_breakfast_burritos_1404_madison_ave_new_york_3235140.csv

| **"Item ID"** | **"Item Name"**                     | **"Modifier Group Name"** | **"Option Name"**        | **"Option Price"** | **"Option Price Currency"** | **"Option Delivery Price"** | **"Option Delivery Price Currency"** | **"Option Pickup Price"** | **"Option Pickup Price Currency"** | **"Modifier Min"** | **"Modifier Max"** | **"Modifier Sequence Number"** | **"Modifier Is Available"** | **"Modifier ID"** | **"Modifier Group Display Type"** |
|---------------|-------------------------------------|---------------------------|--------------------------|--------------------|-----------------------------|-----------------------------|--------------------------------------|---------------------------|------------------------------------|--------------------|--------------------|--------------------------------|-----------------------------|-------------------|-----------------------------------|
| "13828721776" | "No Fuss No Muss Breakfast Burrito" | "Add A Side"              | "Fruit Bowl "            | "5.99"             | "USD"                       | "5.99"                      | "USD"                                | "5.99"                    | "USD"                              | "0"                | "5"                | "1"                            | "True"                      | "13774873083"     | "CHOOSE_MANY_OPTIONAL"            |
| "13828721776" | "No Fuss No Muss Breakfast Burrito" | "Add A Side"              | "Home Fried Potatoes "   | "4.99"             | "USD"                       | "4.99"                      | "USD"                                | "4.99"                    | "USD"                              | "0"                | "5"                | "2"                            | "True"                      | "13774873100"     | "CHOOSE_MANY_OPTIONAL"            |
| "13828721776" | "No Fuss No Muss Breakfast Burrito" | "Add A Side"              | "Bagel and Cream Cheese" | "4.99"             | "USD"                       | "4.99"                      | "USD"                                | "4.99"                    | "USD"                              | "0"                | "5"                | "3"                            | "True"                      | "13774873066"     | "CHOOSE_MANY_OPTIONAL"            |


# Architecture

## File structure
The basic file structure of the project architecture

```
grubhub_crawler             : Main project folder
├── grubhub_crawler.py      : Script crawler runner
├── grubhub                 : Project libraries
│ ├── command_line 
│ │ ├── argument_parser.py  : Define the command line arguments ex: --urls 
│ │ └── display_messages.py : Display the program messages 
│ ├── crawler
│ │ └── restaurants.py      : Crawler integration logic of data getting, extractions and outputs 
│ ├── input
│ │ ├── formaters.py        : Normalizer functions
│ │ ├── json
│ │ │ └── extractors.py     : Extracts and transforms the required data from obtained json data of rest api
│ ├── output
│ │ ├── csv
│ │ │ ├── export_fields.py  : Declare desired the data fields to outputs on CSV file 
│ │ │ └── managers.py       : Manages CSV files data exportations
│ └── rest_api
│     ├── authentication.py : Get the initial clientId required to use on Rest API
│     └── grubhub_api.py    : Communicates with the GrubHub Rest API
└── output_csv              : Write the CSV files here
```

## Advantage of Async calls
The main difference about this tool from another libraries (such: [https://pypi.org/project/grubhub/](https://pypi.org/project/grubhub/)) is the asynchronous architecture speeding up the api data collection much more fast.

To a synchronous architecture collects the restaurant data with menu items and items modifiers takes around 35 secs, because it depends on for each menu item a specific request to get the items modifiers.

But with async.io library it takes around 3 secs, accelerating the IO quantity demanded in the process.

## Reacting on schema change
As the GrubHub site is a constantly evolving product, it is quite common to have data schema changes in the future.

Therefore, it is very simple to adapt these changes, you will have 4 specific points:
- `grubhub.input.json.extractors.JsonDataExtractor`: mapping the new json keys the desired data is found
- `grubhub.output.csv.export_fields.csv_field_names`: forwarding the field names, in case you want to rename some (the extractor must have the same fields as the exporter)
- `grubhub.crawler.restaurants.GrubhubRestaurantSpider`: if any way of obtaining data is changed
- `grubhub.rest_api.grubhub_api.GrubHubAPI`: if you have to change a url, or even if you want to include integration with a new endpoint