import json

import requests
import lxml
from bs4 import BeautifulSoup
from proxy_auth import proxies

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
# ссsлки для url мероприятий
fests_urls_list = []

for i in range(0, 50, 16):
    url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=29%20Jun%202022&to_date=&maxprice=500&o={i}8&bannertitle=July"
    req = requests.get(url=url, headers=headers, proxies=proxies)
    json_data = json.loads(req.text)
    html_response = json_data['html']

    with open(f'data/index_{i}.html', "w") as file:
        file.write(html_response)

    with open(f'data/index_{i}.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all(class_='card-details-link')

    for item in cards:
        fest_url = 'https://www.skiddle.com/' + item.get('href')
        fests_urls_list.append(fest_url)
# print(fests_urls_list)

#перебор каждой ссылки из списка ссылок
count = 0
fest_list_result = []
for url in fests_urls_list:
    count += 1
    print(count)
    print("***")

    req = requests.get(url= url, headers=headers, proxies=proxies)

    try:
        soup = BeautifulSoup(req.text, "lxml")
        fest_info_block = soup.find("div", class_="top-info-cont")

        fest_name = fest_info_block.find("h1").text.strip()
        fest_date = fest_info_block.find("h3").text.strip()
        fest_location_url = "https://www.skiddle.com" + fest_info_block.find("a", class_="tc-white").get("href")

        # get contacts details and info
        req = requests.get(url = fest_location_url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(req.text, "lxml")


        contact_details = soup.find("h2", string="Venue contact details and info").find_next()
        items = [item.text for item in contact_details.find_all("p")]

        contact_details_dict = {}
        for contact_details in items:
            contact_details_list = contact_details.split(":")
            if len(contact_details_list) == 3:
                contact_details_dict[contact_details_list[0].strip()] = contact_details_list[1].strip() +":"\
                                                                            + contact_details_list[2].strip()
            else:
                contact_details_dict[contact_details_list[0].strip()] = contact_details_list[1].strip()


            print(contact_details)

        fest_list_result.append(
            {
                "Fest name": fest_name,
                "Fest date": fest_date,
                "Contacts": contact_details_dict
            }
        )

    except Exception as ex:
        print(ex)
        print('Ошибка')

with open('fest_list_result.json', 'a', encoding='utf-8') as file:
    json.dump(fest_list_result, file, indent=4, ensure_ascii=False)