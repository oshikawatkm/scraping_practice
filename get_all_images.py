from selenium import webdriver
from PIL import Image
import io
from urllib import request

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://scraping-for-beginner.herokuapp.com/image')

elems = browser.find_elements_by_class_name('material-placeholder')

for index, elem in enumerate(elems):
    elem = elem.find_element_by_tag_name('img')
    url = elem.get_attribute('src')
    f = io.BytesIO(request.urlopen(url).read())
    img = Image.open(f)
    img.save('image/image{}.png'.format(index))
