import html

import requests
from bs4 import BeautifulSoup
import urllib

# text = 'наруто и саске'
# text.replace(' ', '%20')
# url = 'https://yandex.ru/images/search?text=' + text + '&isize=eq&iw=1080&ih=1920'
# r = requests.get(url)
# # with open('test.html', 'w', encoding='utf8') as output_file:
# #     output_file.write(r.text)
#
#
# soup = BeautifulSoup(r.text, 'lxml')
# images_list = soup.find_all('a', {'class': 'serp-item__link'})
# list = []
# for image in images_list:
#     url = 'https://yandex.ru' + image.get('href')
#     r = requests.get(url)
#     txt = html.unescape(r.text)
#     soup = BeautifulSoup(urllib.parse.unquote(r.text), 'lxml')
#     #list.append(soup.find('img', {'class': 'MMImage-Origin'}))
# print(list)

import selenium
from selenium.webdriver.chrome import webdriver

DRIVER_PATH = '../venv/Lib/site-packages/selenium'
wd = webdriver.Chrome(executable_path=DRIVER_PATH)
wd.get('https://google.com')
search_box = wd.find_element_by_css_selector('input.gLFyf')

search_box.send_keys('Dogs')






