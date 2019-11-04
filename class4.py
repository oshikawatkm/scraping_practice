import pandas as pd
from selenium import webdriver
df = pd.DataFrame

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')
elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')
elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()

keys = []

elems_th = browser.find_elements_by_tag_name('th')

for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

values = []

elems_td = browser.find_elements_by_tag_name('td')

for elem_td in elems_td:
    value = elem_td.text
    if value.find('\n'):
        value.split('\n')
        value = value[0]

    values.append(value)

df['項目'] = keys
df['値'] = values

df.to_csv('講師情報.csv', index=False)