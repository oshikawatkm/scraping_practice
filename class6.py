from selenium import webdriver
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://scraping-for-beginner.herokuapp.com/ranking/')

elems_rankingBox = browser.find_elements_by_class_name('u_areaListRankingBox')
elems_tips = browser.find_elements_by_class_name('u_categoryTipsItem')

titles = []
values = []

for elem_rankingBox in elems_rankingBox:
    elem_title = elem_rankingBox.find_element_by_class_name('u_title')
    title = elem_title.text.split('\n')[1]
    titles.append(title)
    for elem_tip in elems_tips:
        elem_value = elem_tip.find_element_by_class_name('evaluateNumber')
        value = elem_value.text
        values.append(value)

print(values)