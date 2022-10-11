import requests
import json

def get_data():
    cookies = {
        '_ym_uid': '1588781662138743869',
        'cfidsgib-w-mvideo': 'lzVXCI5H/RPjAe8+E/zzrRUgpkd5/q53oxmx9IEws7Myn7mwoT6dPdl94dNPN93FWx63ip2VzBTanTtHsshVwKFfieTIRvArJKfCFy/ckKiPWPBQCJn8p0rRWVt+HtH9i0338qwuE5x/n4VzE0ujlV5PJEsAsIujUoGt',
        '__lhash_': '81cb612565c9bab73274ff66b44b98e5',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_2_exp_in_1': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GTM_DELAY': 'true',
        'MVID_GUEST_ID': '21002909548',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '2',
        'MVID_MCLICK': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '3',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '_gid': 'GA1.2.713996649.1657017364',
        '_ym_d': '1657017364',
        '_ym_isad': '1',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '8494c17900f3687b683ced2ed68878b6',
        'tmr_lvidTS': '1588781669474',
        'advcake_session_id': 'bdef18cc-f63c-15a1-799b-7cb48a12cfd0',
        'advcake_track_id': 'b854ee16-b0f9-09b8-7c27-0b0b0f482c66',
        'flocktory-uuid': '56f1aa2e-2c22-4a81-9515-1064a71c00f3-0',
        'AF_SYNC': '1657017368212',
        'afUserId': 'cdbceefd-6002-46a8-86e1-39f67ac9d625-o',
        '__js_p_': '314,900,0,1,0',
        'MVID_CITY_ID': 'CityCZ_6273',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'MVID_REGION_ID': '21',
        'MVID_REGION_SHOP': 'S929',
        'MVID_TIMEZONE_OFFSET': '4',
        'MVID_CART_AVAILABILITY': '2',
        'MVID_CITY_CHANGED': 'false',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_KLADR_ID': '1800000100000',
        'MVID_ENVCLOUD': 'prod2',
        'mindboxDeviceUUID': 'b797c140-2d30-4687-86f8-965fe8ded8b4',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22b797c140-2d30-4687-86f8-965fe8ded8b4%22%7D',
        '_ga': 'GA1.2.596009591.1657017364',
        'tmr_detect': '1%7C1657020171684',
        'tmr_reqNum': '202',
        'JSESSIONID': 'YpQsvGgL1c2qssLjGLd8gspbJn2qzLJBXhTHyw3PTnhLvzDThVn1!196722648',
        'bIPs': '155255760',
        '_ga_CFMZTSS5FM': 'GS1.1.1657017364.1.1.1657020552.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1657017364.1.1.1657020552.60',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ym_uid=1588781662138743869; cfidsgib-w-mvideo=lzVXCI5H/RPjAe8+E/zzrRUgpkd5/q53oxmx9IEws7Myn7mwoT6dPdl94dNPN93FWx63ip2VzBTanTtHsshVwKFfieTIRvArJKfCFy/ckKiPWPBQCJn8p0rRWVt+HtH9i0338qwuE5x/n4VzE0ujlV5PJEsAsIujUoGt; __lhash_=81cb612565c9bab73274ff66b44b98e5; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_2_exp_in_1=2; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GTM_DELAY=true; MVID_GUEST_ID=21002909548; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=2; MVID_MCLICK=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=3; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _gid=GA1.2.713996649.1657017364; _ym_d=1657017364; _ym_isad=1; SMSError=; authError=; tmr_lvid=8494c17900f3687b683ced2ed68878b6; tmr_lvidTS=1588781669474; advcake_session_id=bdef18cc-f63c-15a1-799b-7cb48a12cfd0; advcake_track_id=b854ee16-b0f9-09b8-7c27-0b0b0f482c66; flocktory-uuid=56f1aa2e-2c22-4a81-9515-1064a71c00f3-0; AF_SYNC=1657017368212; afUserId=cdbceefd-6002-46a8-86e1-39f67ac9d625-o; __js_p_=314,900,0,1,0; MVID_CITY_ID=CityCZ_6273; MVID_GEOLOCATION_NEEDED=false; MVID_REGION_ID=21; MVID_REGION_SHOP=S929; MVID_TIMEZONE_OFFSET=4; MVID_CART_AVAILABILITY=2; MVID_CITY_CHANGED=false; MVID_CREDIT_AVAILABILITY=true; MVID_KLADR_ID=1800000100000; MVID_ENVCLOUD=prod2; mindboxDeviceUUID=b797c140-2d30-4687-86f8-965fe8ded8b4; directCrm-session=%7B%22deviceGuid%22%3A%22b797c140-2d30-4687-86f8-965fe8ded8b4%22%7D; _ga=GA1.2.596009591.1657017364; tmr_detect=1%7C1657020171684; tmr_reqNum=202; JSESSIONID=YpQsvGgL1c2qssLjGLd8gspbJn2qzLJBXhTHyw3PTnhLvzDThVn1!196722648; bIPs=155255760; _ga_CFMZTSS5FM=GS1.1.1657017364.1.1.1657020552.0; _ga_BNX5WPP3YK=GS1.1.1657017364.1.1.1657020552.60',
        'dnt': '1',
        'referer': 'https://www.mvideo.ru/product-list-page/f/skidka=da/tolko-v-nalichii=da?q=%D0%BF%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82&category=planshety-195',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-set-application-id': '9e76f11b-9e35-4d08-bdaf-45c4455ce66e',
    }

    params = {
        'query': 'планшет',
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
        'context': 'eyJxdWVyeSI6ItC_0LvQsNC90YjQtdGCIiwic2hvcElkcyI6WyJTOTI5Il0sInN0cmF0ZWd5SWQiOiJzdGVwMSIsImhpZGRlbkZpcnN0R3JvdXAiOltdLCJmaXJzdEdyb3VwIjpbXSwicmVzcG9uc2VUeXBlIjoicGxhaW4iLCJiaVN0YXRzIjp7fX0=',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/search', params=params, cookies=cookies, headers=headers).json()
    # print(response)
    products_ids = response.get('body').get('products')

    with open('data/1_products_id.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('data/2_items.json', 'w', encoding='utf8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('data/3_price.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_base_price': item_base_price,
            'item_sale_price': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('data/4_items_prices.json', 'w', encoding='utf8') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

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
    get_result()

if __name__ == '__main__':
     main()