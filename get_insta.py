from selenium import webdriver
from PIL import Image
import io
from urllib import request

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://www.instagram.com/i_ro_i_ro_i/')

elems = browser.find_elements_by_class_name('KL4Bh')

for index, elem in enumerate(elems):
    elem = elem.find_element_by_tag_name('img')
    url = elem.get_attribute('src')
    print(url)