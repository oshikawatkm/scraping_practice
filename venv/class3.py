from selenium import webdriver

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')
elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()

keys = []

elems_td = browser.find_elements_by_tag_name('td')

for elem_td in elems_td:
    key = elem_td.text
    print(key)
    keys.append(key)