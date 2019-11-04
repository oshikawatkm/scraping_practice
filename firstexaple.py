import requests

url = 'http://www.webscrapingfordatascience.com/basichttp'
r = requests.get(url)
print(r.request.headers)