from selenium import webdriver

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://localhost:3000/pin_orders')

div = []
div = browser.find_elements_by_tag_name('div')
print(len(div))

sdiv = []
sdiv = browser.browser.find_elements_by_tag_name('/div')
print(len(sdiv))