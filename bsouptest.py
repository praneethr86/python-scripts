import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.thehindu.com/opinion/editorial/")
soup = BeautifulSoup(page.content, 'html.parser')

news_feed = soup.find(class_="100_4x_2EditorialStories")

# all_news_content = news_feed.find_all(class_="ES2-100x4-text1-heading")
all_news_content = news_feed.find_all('a', href=True)

for item in all_news_content:
    link = item['href']
    print(item.text)
    article = requests.get(link)
    souparticle = BeautifulSoup(article.content, 'html.parser')
    newsarticle = souparticle.find(class_='article')
    articlecontent = newsarticle.find_all('p')
    for articletext in articlecontent:
        print(articletext.text)




#hindu : .100_4x_2EditorialStories, find h2 and a in that

