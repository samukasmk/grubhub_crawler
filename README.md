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

**Simple collection:** collect just basic information such as:
 - (from restaurant): restaurant name, address, city, state, stars, review count
 - (from menu items): category name, item name, item description, item price
 - (from modifiers items): modifier group name, modifier min, modifier max, option name, option price

**Full collection:** collects much information as possible as too:
 - (from menu items): category or item is available, item is popularity, item price for delivery or pickup, tax rate, ...
 - (from modifiers items): modifier availability, option price for delivery or pickup, ...

--collect-all-information

### Executing the Simple collection
This is the default option when you execute de command line, follow a example of command line execution for a **simple collection**:
```bash
$ python grubhub_crawler.py \
  --urls https://www.grubhub.com/restaurant/dosa-love-893-e-el-camino-real-sunnyvale/3024935 \
         https://www.grubhub.com/restaurant/beaus-breakfast-burritos-1404-madison-ave-new-york/3235140 \
         https://www.grubhub.com/restaurant/impeckable-wings-901-nw-24th-st-san-antonio/3159434 \
         https://www.grubhub.com/restaurant/the-vegan-grill-5155-3rd-st-san-francisco/2994242
```
Follow the sample of output for the **simple collection**:
```
[GrubHub Restaurant Crawler]

Getting restaurants data:
----------------------------------------------------------------------------------------------------------------------------------------------------------------
-> (1) Restaurant URL: https://www.grubhub.com/restaurant/dosa-love-893-e-el-camino-real-sunnyvale/3024935
       Crawler state: succes
       Restaurant Name: Dosa Love
       Restaurant Address: 893 E El Camino Real
       Restaurant City: Sunnyvale
       Restaurant State: CA
       Restaurant Stars: 4
       Restaurant Review Count: 12
       CSV file (menu items): ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_dosa_love_893_e_el_camino_real_sunnyvale_3024935.csv
       CSV file (items modifiers): ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_dosa_love_893_e_el_camino_real_sunnyvale_3024935.csv
----------------------------------------------------------------------------------------------------------------------------------------------------------------
-> (2) Restaurant URL: https://www.grubhub.com/restaurant/beaus-breakfast-burritos-1404-madison-ave-new-york/3235140
       Crawler state: succes
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
       Crawler state: succes
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
       Crawler state: succes
       Restaurant Name: The Vegan Grill
       Restaurant Address: 5155 3rd St
       Restaurant City: San Francisco
       Restaurant State: CA
       Restaurant Stars: 3
       Restaurant Review Count: 10
       CSV file (menu items): ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_the_vegan_grill_5155_3rd_st_san_francisco_2994242.csv
       CSV file (items modifiers): ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_the_vegan_grill_5155_3rd_st_san_francisco_2994242.csv
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Elapsed time: 0:00:04.063403
```

## Output files to CSV format
For a **simple collection 
### Sample content of CSV file for (menu items):
> **File path:** ./output_csv/menu_downloads_https___www.grubhub.com_restaurant_dosa_love_893_e_el_camino_real_sunnyvale_3024935.csv

| **Category Name** | **Item Name**                          | **Item Description**                                                                                                                                                                                                                       | **Item Price** |
|-------------------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Combos            | Combo1 - Idli (3) Vada(1)              | Steamed savory cakes made from rice and lentil batter fluffy & soft Idli (3), Crispy savory doughnuts made of Urad lentils batter deep fried (1), served with 3 chutneys and sambar on the side                                            | 9.99           |
| Combos            | Combo2 - Idli (1) Vada(1) & Plain Dosa | Steamed savory cakes made from rice and lentil batter fluffy & soft Idli (1),  Crispy savory doughnuts made of Urad lentils batter deep fried (1), Savory crepe made of rice & lentil batter served with 3 chutneys and sambar on the side | 10.5           |
| Standout Starters | Mt. Mirchi Bhaji                       | (ONLY AVAILABLE AFTER 11:30AM. IF ORDERED BEFORE THAT TIME, IT WILL NOT BE INCLUDED IN ORDER) Serrano Chilies coated with besan flour and spices deep fried – served with chutney                                                          | 7.69           |
| Standout Starters | Cut To The Mirchi                      | (ONLY AVAILABLE AFTER 11:30AM. IF ORDERED BEFORE THAT TIME, IT WILL NOT BE INCLUDED IN ORDER) Serrano Chilies coated with besan flour and spices deep fried, cut into pieces – served with chutney                                         | 7.69           |
| ...               | ...                                    | ...                                                                                                                                                                                                                                        | ...            |


### Sample content of CSV file for (modifiers items):
> **File path:** ./output_csv/modifier_downloads_https___www.grubhub.com_restaurant_dosa_love_893_e_el_camino_real_sunnyvale_3024935.csv

| **Modifier Group Name** | **Modifier Min** | **Modifier Max** | **Option Name**    | **Option Price** |
|-------------------------|------------------|------------------|--------------------|------------------|
| Additional Sides        | 0                | 5                | Single Idli        | 2.5              |
| Additional Sides        | 0                | 5                | Single Vada        | 2.5              |
| Additional Sides        | 0                | 5                | Yogurt Rice 16Oz   | 7.15             |
| Additional Sides        | 0                | 5                | Bisibele Bath 16Oz | 7.15             |
| Additional Sides        | 0                | 5                | Tamarind Rice 16Oz | 7.15             |
| Additional Drinks       | 0                | 6                | Coke               | 1.75             |
| Additional Drinks       | 0                | 6                | Diet Coke          | 1.75             |
| Additional Drinks       | 0                | 6                | Sprite             | 1.75             |
| Additional Drinks       | 0                | 6                | Butter MIlk        | 2.99             |
| ...                     | ...              | ...              | ...                | ...              |


# Development
## File structure

## Async architecture

## React on layout on schema change