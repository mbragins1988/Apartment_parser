from time import sleep

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

where_flat = str(input())

browser = Chrome()

number_pages = 101

url = 'https://www.avito.ru/sochi?q=купить'

browser.get(url)

input_where_flat = browser.find_element(By.CLASS_NAME, 'input-input-Zpzc1')
input_where_flat.send_keys(f' {where_flat}')
input_where_flat.send_keys(Keys.ENTER)


def data():
    for _ in range(number_pages):
        soup = BeautifulSoup(browser.page_source, 'lxml')
        flats = soup.findAll('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')

        for flat in flats:
            name = flat.find('h3', class_='styles-module-root-TWVKW styles-module-root-_KFFt styles-module-size_l-_oGDF styles-module-size_l-hruVE styles-module-ellipsis-LKWy3 styles-module-weight_bold-Kpd5F stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-header-l-qvNIS').text.strip()
            location = flat.find('p', class_='styles-module-root-_KFFt styles-module-size_s-awPvv styles-module-size_s-_P6ZA styles-module-ellipsis-LKWy3 styles-module-ellipsis_oneLine-NY089 stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-paragraph-s-_c6vD styles-module-root_top-HYzCt styles-module-margin-top_0-_usAN').text.strip()
            price = flat.find('strong', class_='styles-module-root-LIAav').text.strip()
            link = 'https://www.avito.ru' + flat.find('a', class_='styles-module-root-QmppR styles-module-root_noVisited-aFA10').get('href')
            data = (flat.find('p', class_='styles-module-root-_KFFt styles-module-size_s-awPvv styles-module-size_s-_P6ZA stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-paragraph-s-_c6vD styles-module-noAccent-nZxz7').text.strip()).split(' ')
            if (
                str(data[1]) == 'часа' or str(data[1]) == 'часов'
                or str(data[1]) == 'час' or str(data[1]) == 'минут'
                or str(data[1]) == 'минуты' or str(data[1]) == 'день'
            ) and (price.split('\xa0')[-1] != 'за сутки'
                    and price.split('\xa0')[-1] != 'в месяц'):
                yield name, price, location, link
        browser.find_element(By.CLASS_NAME, 'ArrowIcon-module-root_direction_right-zm8km').click()
        sleep(5)
