from selenium import webdriver

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://scraping-for-beginner.herokuapp.com')

xpath = '/html/body/div[2]/div/div/div[1]/ul/li[1]'
print(browser.find_element_by_xpath(xpath).text)