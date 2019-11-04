from selenium import webdriver
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://scraping-for-beginner.herokuapp.com/ranking/')

elem_rankingBox = browser.find_element_by_class_name('u_areaListRankingBox')
elem_title =elem_rankingBox.find_element_by_class_name('u_title')
title = elem_title.text
title.split('\n')
print(title)

elem_value = elem_rankingBox.find_element_by_class_name('u_rankBox').find_element_by_class_name('evaluateNumber')
value = elem_value.text
print(value)

elem_category_title = browser.find_element_by_class_name('u_categoryTipsItem')
elem_fine = elem_category_title.find_element_by_class_name('is_rank').find_element_by_class_name('evaluateNumber')
fine = elem_fine.text
print(fine)