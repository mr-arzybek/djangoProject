import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = 'https://cars.kg/offers'

HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
}


# start
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# get data
@csrf_exempt
def get_data(html):
    soup = bs(html, "html.parser")
    items = soup.find_all('a', class_='catalog-list-item')
    car_items = []

    for item in items:
        car_items.append(
            {
                'title_name': item.find('a', class_='catalog-item-caption').get_text(),
                'title_url': item.find('a').get('href'),
                'image': item.find('span', class_='catalog-item-cover').find('img').get('src'),
            }
        )

    return car_items


# EndParse
@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        rezka_film2 = []
        for page in range(0, 1):
            html = get_html(f'https://m.cars.kg/offers#1', params=page)
            rezka_film2.extend(get_data(html.text))
        return rezka_film2
    else:
        raise Exception('Error in parser')
