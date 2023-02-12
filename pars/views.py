from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from . import serializers
from .models import Hotel


class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = serializers.HotelListSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]


# import requests
# from bs4 import BeautifulSoup
# from .models import Hotel


# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     product_list = soup.find('div', class_='layout-3 new-real-estate-srp').find('div', class_='col-2 new-real-estate-srp')
#     products = product_list.find_all('div', class_='clearfix')

#     for product in products:
#         # try:
#         #     title = product.find('div', class_ = 'title').find('a').text.strip()
#         # except:
#         #     title ='---'
#         try:
#             image = product.find('div', class_='left-col').find('div', class_='image').find('img').get('src')
#         except:
#             image ='---'
#         try:
#             price = product.find('div', class_='price').text.strip()[1:]
#             currency = product.find('div', class_='price').text.strip()[0]
#         except:
#             price = '---'
#             currency = '---'
#         try:
#             date = product.find('div', class_='location').find('span', class_='date-posted').text
#             # return date
#         except:
#             date ='---'

#         data = {'image': image, 'price': price, 'currency': currency, 'date': date}

#         my_model = Hotel(image=image, price=price, currency=currency, date=date)
#         my_model.save()
    


# def get_html(url):
#     # headers = { '“Authorization”' : '”our_unique_secret_token”' }
#     headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
#     response = requests.get(url, headers=headers)
#     return response.text


# def parsing_of_website():
#     url1 = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273?ad=offering'
#     get_page_data(get_html(url='https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273?ad=offering'))
    
# parsing_of_website()

