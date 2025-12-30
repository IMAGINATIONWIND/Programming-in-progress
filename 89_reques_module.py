import requests
from bs4 import BeautifulSoup
# response = requests.get("https://roadmap.sh/")
#can be used for web scraping of static webpages/sites
#

url = "https://books.toscrape.com/"
r = requests.get(url)

soup = BeautifulSoup(r.text , "html.parser")
print(soup.prettify())


# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'sushant',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }

# response = requests.post(url,headers=headers,json=data)

# print(response.text)