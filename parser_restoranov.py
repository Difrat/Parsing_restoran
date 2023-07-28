import time
import datetime
import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

start_time = time.time()
balance = {}
href_all_cities = []
ua = UserAgent()
all_links_restoran = []
all_links = []


def view_all() -> list:
    cookies = {
        'PHPSESSID': '4ba4ffec4dbc1cb6f3beb5fd54cfadb1',
        '_gcl_au': '1.1.917440639.1689507899',
        'localization_popup_hide': '1',
        '_ga': 'GA1.2.1101217918.1689507908',
        'promo_img': '1',
        'hl': 'ru_RU',
        '__cf_bm': 'B7uYV4aBMlNZO9eEEhP30LJDV2TfcVCVoMVluWaVNhI-1690093428-0-AQwWXX0kqLsCZm+ogS+0yHuYPsve/LJxdPygdXPh8DoN9hToZtZWIwzNY7P9tfaefTrSWGvJl9STGxluEtsEguo=',
        'client_time_hour': '2023-07-23%2016:25:14',
        'rg_check': '1',
        'banner_show': '1',
        '_gid': 'GA1.2.1635457070.1690093515',
        '_gat': '1',
        '_ga_N0PX6VDPSG': 'GS1.2.1690093515.5.0.1690093515.0.0.0',
        'pier_tutor_nums': '%7B%22nums%22%3A%5B4%2C5%2C1%2C3%2C2%5D%2C%22current%22%3A4%7D',
    }

    headers = {
        'authority': 'ru.restaurantguru.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'https://kwork.ru/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': f'{ua.random}',
    }
    href_city = None
    try:
        response = requests.get('https://ru.restaurantguru.com/cities-Georgia-c', cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        cities = soup.find('div', class_='wrapper_blocks').find_all('a', class_='show_all show_all_btn')
        href_city = [city.get('href') for city in cities]
    except Exception as ex:
        print(ex)
    return href_city


def get_cities_view_all(list_alp: list):
    cookies = {
        'PHPSESSID': '4ba4ffec4dbc1cb6f3beb5fd54cfadb1',
        '_gcl_au': '1.1.917440639.1689507899',
        'localization_popup_hide': '1',
        '_ga': 'GA1.2.1101217918.1689507908',
        'promo_img': '1',
        'hl': 'ru_RU',
        '__cf_bm': 'B7uYV4aBMlNZO9eEEhP30LJDV2TfcVCVoMVluWaVNhI-1690093428-0-AQwWXX0kqLsCZm+ogS+0yHuYPsve/LJxdPygdXPh8DoN9hToZtZWIwzNY7P9tfaefTrSWGvJl9STGxluEtsEguo=',
        'client_time_hour': '2023-07-23%2016:25:14',
        'rg_check': '1',
        'banner_show': '1',
        '_gid': 'GA1.2.1635457070.1690093515',
        '_gat': '1',
        '_ga_N0PX6VDPSG': 'GS1.2.1690093515.5.0.1690093515.0.0.0',
        'pier_tutor_nums': '%7B%22nums%22%3A%5B4%2C5%2C1%2C3%2C2%5D%2C%22current%22%3A4%7D',
    }

    headers = {
        'authority': 'ru.restaurantguru.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'https://kwork.ru/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': f'{ua.random}',
    }
    for url in list_alp:
        response = requests.get(url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        cities_in_section = soup.find('ul', class_='cities-list clearfix clear scroll-container').find_all('a')
        # cities_span = soup.find('ul', class_='cities-list clearfix clear scroll-container').find_all('span',
        #                                                                                              class_='city_name')
        cities_name = [city.get('href').split('/')[-1] for city in cities_in_section]
        # cities_name = [city.text for city in cities_span]
        restoran_span = soup.find('ul', class_='cities-list clearfix clear scroll-container').find_all('span',
                                                                                                     class_='city-cnt')
        restoran_total = [int(restoran.text.strip()) for restoran in restoran_span]
        balance.update({f'{x}': y for x, y in zip(cities_name, restoran_total)})
        href_all_cities.extend([city.get('href') for city in cities_in_section])
        time.sleep(1 / 3)


def get_empty_view_all():
    cities_list_href = []
    cookies = {
        'PHPSESSID': '4ba4ffec4dbc1cb6f3beb5fd54cfadb1',
        '_gcl_au': '1.1.917440639.1689507899',
        'localization_popup_hide': '1',
        '_ga': 'GA1.2.1101217918.1689507908',
        'promo_img': '1',
        'hl': 'ru_RU',
        '__cf_bm': 'B7uYV4aBMlNZO9eEEhP30LJDV2TfcVCVoMVluWaVNhI-1690093428-0-AQwWXX0kqLsCZm+ogS+0yHuYPsve/LJxdPygdXPh8DoN9hToZtZWIwzNY7P9tfaefTrSWGvJl9STGxluEtsEguo=',
        'client_time_hour': '2023-07-23%2016:25:14',
        'rg_check': '1',
        'banner_show': '1',
        '_gid': 'GA1.2.1635457070.1690093515',
        '_gat': '1',
        '_ga_N0PX6VDPSG': 'GS1.2.1690093515.5.0.1690093515.0.0.0',
        'pier_tutor_nums': '%7B%22nums%22%3A%5B4%2C5%2C1%2C3%2C2%5D%2C%22current%22%3A4%7D',
    }

    headers = {
        'authority': 'ru.restaurantguru.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'https://kwork.ru/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': f'{ua.random}'
    }
    response = requests.get('https://ru.restaurantguru.com/cities-Georgia-c', cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    cities_empty_view_all = soup.find('div', class_='wrapper_blocks').find_all('div', class_='cities_block')
    cities_list = [item.find_all('a') for item in cities_empty_view_all
                   if item.find('a', class_='show_all show_all_btn') == None]
    for n in cities_list:
        cities_list_href.extend(n)
        balance.update({f'{x}': y for x, y in zip([city.get('href').split('/')[-1] for city in n], [int(num.find('span',
                                                                        class_='grey').text.split()[-1]) for num in n])})

    href_all_cities.extend([item.get('href') for item in cities_list_href])


def get_all_restoran_in_city(cities_all_link: list):
    for link in cities_all_link:
        n = 1
        restoran = []
        while True:
            headers = {
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Referer': f'{link}',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua-mobile': '?0',
                'User-Agent': f'{ua.random}',
            }

            params = {
                'skip_geo': '1',
            }
            city = link.split('/')[-1]
            response = requests.get(f'https://ru.restaurantguru.com/restaurant-{city}-t1/{n}', params=params,
                                    headers=headers)
            text = response.text.replace('\\', '')
            soup = BeautifulSoup(text, 'lxml')
            div_class = soup.find_all('div', class_='restaurant_row')
            href = [x.get('data-review-href') for x in div_class]
            if len(href) == 0:
                break
            restoran.extend(href)
            n += 1
            time.sleep(1 / 3)
        print(len(restoran), city)
        all_links.extend(restoran)


def main():
    get_cities_view_all(view_all())
    get_empty_view_all()
    get_all_restoran_in_city(href_all_cities)
    print(len(all_links))
    print(len(set(all_links)))
    current_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
    finish_time = time.time() - start_time
    print(f'{finish_time}')


if __name__ == '__main__':
    main()
