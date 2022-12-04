import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

from src.utils.constants import MWP_URL, MWP_ROOT_PATH

response = requests.post(MWP_URL)
soup = BeautifulSoup(response.text, 'html.parser')

devices_list = []
prices_list = []
raw_features_list = []
brands_links = soup.find_all('a', href=re.compile('-mobile-prices-usa'))

for link in brands_links:
    brand_url = MWP_ROOT_PATH+link['href']
    brand_response = requests.post(brand_url)
    brand_soup = BeautifulSoup(brand_response.text, 'html.parser')
    pages = brand_soup.find_all('a', {'class': "pageination"})
    models = brand_soup.find_all('div', {'class': "pro-name"})
    prices = brand_soup.find_all('div', {'class': "price"})
    for model in models:
        devices_list.append(model.text)
    for price in prices:
        prices_list.append(price.text)
    if len(pages) > 1:
        for i in range(len(pages)):
            if i == 6 or i == (len(pages)-1):
                break
            elif i > 0:
                page_url = MWP_ROOT_PATH + pages[i]['href']
                print(page_url)
                page_response = requests.post(page_url)
                page_soup = BeautifulSoup(page_response.text, 'html.parser')
                models = page_soup.find_all('div', {'class': "pro-name"})
                prices = page_soup.find_all('div', {'class': "price"})
                # phone_links = soup.find_all('a', href=re.compile('-in-usa-5030.php'))
                for model in models:
                    devices_list.append(model.text)
                for price in prices:
                    prices_list.append(price.text)
                    """
                for phone in phone_links:
                    phone_url = MWP_ROOT_PATH + phone['href']
                    phone_response = requests.post(phone_url)
                    phone_soup = BeautifulSoup(phone_response.text, 'html.parser')
                    phone_text = phone_soup.find(text=re.compile('Released in'))
                    if phone_text is not None:
                        raw_features_list.append(phone_text.text)
                        """

print(len(devices_list))
print(len(prices_list))
print(len(raw_features_list))

# devices_df = pd.DataFrame(list(zip(devices_list, prices_list, raw_features_list)),
                          # columns=['model', 'price', 'raw_features'])

devices_df = pd.DataFrame(list(zip(devices_list, prices_list)),
                          columns=['model', 'price'])

devices_df.to_csv('devices_list.csv', sep=',', encoding='utf-8')
