from selenium import webdriver
import pandas as pd

df = pd.DataFrame()
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://scraping-for-beginner.herokuapp.com/ranking')

elems_rankingBox = browser.find_elements_by_class_name('u_areaListRankingBox')
elems = browser.find_elements_by_class_name('u_categoryTipsItem')
elems_rank = browser.find_elements_by_class_name('u_rankBox')

titles = []
for elem_rankingBox in elems_rankingBox:
    elem_title = elem_rankingBox.find_element_by_class_name('u_title')
    title = elem_title.text.split('\n')[1]
    titles.append(title)


ranks = []
for elem_rank in elems_rank:
    elem_rank = elem_rank.find_element_by_class_name('evaluateNumber')
    rank = float(elem_rank.text)
    ranks.append(rank)


categories = []
for elem in elems:
    elems_tip = elem.find_elements_by_class_name('is_rank')
    _ranks = []
    for elem_tip in elems_tip:
        rank = elem_tip.find_element_by_class_name('evaluateNumber')
        _ranks.append(float(rank.text))
    categories.append(_ranks)

df['観光地名'] = titles
df['総合評価'] = ranks
df_categories = pd.DataFrame(categories)
df_categories.columns = ['楽しさ', '人混みの多さ', '景色', 'アクセス']
df = pd.concat([df, df_categories], axis=1)

df.to_csv('観光地情報.csv', index=False)