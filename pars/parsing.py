import requests
from bs4 import BeautifulSoup
from .models import Hotel
from django.http import HttpResponse



def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find('div', class_='layout-3 new-real-estate-srp').find('div', class_='col-2 new-real-estate-srp')
    products = product_list.find_all('div', class_='clearfix')

    for product in products:
        # try:
        #     title = product.find('div', class_ = 'title').find('a').text.strip()
        # except:
        #     title ='---'
        try:
            image = product.find('div', class_='left-col').find('div', class_='image').find('img').get('src')
        except:
            image ='---'
        try:
            price = product.find('div', class_='price').text.strip()[1:]
            price = int(price.replace(',', '').replace('.', '')[:-2])
            currency = product.find('div', class_='price').text.strip()[0]
        except:
            price = 1
            currency = '---'
        try:
            date = product.find('div', class_='location').find('span', class_='date-posted').text
            # return date
        except:
            date ='---'

        data = {'image': image, 'price': price, 'currency': currency, 'date': date}

        my_model = Hotel(image=image, price=price, currency=currency, date=date)
        my_model.save()
    


def get_html(url):
    # headers = { '“Authorization”' : '”our_unique_secret_token”' }
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers)
    return response.text


def parsing_of_website(request):
    url1 = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273?ad=offering'
    get_page_data(get_html(url='https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273?ad=offering'))
    return HttpResponse('Parsed')
    
# parsing_of_website()

# def update_parse():
    # parsing_of_website()

import schedule
import time

# update_parse()

# schedule.every(1).minute.do(update_parse)

# while True:
#     schedule.run_pending()
#     time.sleep(1)