import requests
import json
from config import headers, cookies
import os
import math

def get_data():
    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ=='
    }

    if not os.path.exists('data'):
        os.mkdir('data')

    s = requests.Session()
    response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    # print(response)

    total_items = response.get('body').get('total')

    if total_items is None:
        return '[!] No items'

    pages_count = math.ceil(total_items / 24)

    print(f'[INFO] Total positions: {total_items} | Total pages: {pages_count}')

    # products_ids = response.get('body').get('products')
    #
    # with open('1_products_id.json', 'w') as file:
    #     json.dump(products_ids, file, indent=4, ensure_ascii=False)
    #
    # # print(products_ids)
    # json_data = {
    #     'productIds': products_ids,
    #     'mediaTypes': [
    #         'images',
    #     ],
    #     'category': True,
    #     'status': True,
    #     'brand': True,
    #     'propertyTypes': [
    #         'KEY',
    #     ],
    #     'propertiesConfig': {
    #         'propertiesPortionSize': 5,
    #     },
    #     'multioffer': False,
    # }
    #
    # response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
    #                          json=json_data).json()
    #
    # with open('2_items.json', 'w', encoding='utf8') as file:
    #     json.dump(response, file, indent=4, ensure_ascii=False)
    #
    # # print(len(response.get('body').get('products')))
    #
    # products_ids_str = ','.join(products_ids)
    #
    # params = {
    #     'productIds': products_ids_str,
    #     'addBonusRubles': 'true',
    #     'isPromoApplied': 'true',
    # }
    #
    # response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
    #                         headers=headers).json()
    #
    # with open('3_price.json', 'w', encoding='utf-8') as file:
    #     json.dump(response, file, indent=4, ensure_ascii=False)
    #
    # items_prices = {}
    #
    # material_prices = response.get('body').get('materialPrices')
    #
    # for item in material_prices:
    #     item_id = item.get('price').get('productId')
    #     item_base_price = item.get('price').get('basePrice')
    #     item_sale_price = item.get('price').get('salePrice')
    #     item_bonus = item.get('bonusRubles').get('total')
    #
    #     items_prices[item_id] = {
    #         'item_base_price': item_base_price,
    #         'item_sale_price': item_sale_price,
    #         'item_bonus': item_bonus
    #     }
    #
    # with open('4_items_prices.json', 'w', encoding='utf8') as file:
    #     json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('data/2_items.json') as file:
        products_data = json.load(file)

    with open('data/4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrise'] = prices.get('item_basePrise')
        item['item_salePrise'] = prices.get('item_salePrise')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w', encoding='utf-8-sig') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    # get_result()

if __name__ == '__main__':
     main()