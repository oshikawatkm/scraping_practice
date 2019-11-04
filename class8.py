from selenium import webdriver
from PIL import Image
import io
from urllib import request

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://scraping-for-beginner.herokuapp.com/image')

elem = browser.find_element_by_class_name('material-placeholder')
elem = elem.find_element_by_tag_name('img')
url = elem.get_attribute('src')
f = io.BytesIO(request.urlopen(url).read())
img = Image.open(f)
img.save('img01.jpg')