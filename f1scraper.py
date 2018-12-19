import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.espn.in/f1/")

soup = BeautifulSoup(page.content, 'html.parser')

news_feed = soup.find(id="news-feed")

all_news_content = news_feed.find_all(class_="contentItem__content")

for item in all_news_content:
	header = item.find(class_="contentItem__title")
	subhead = item.find(class_="contentItem__subhead")
	print("*Article: " + header.get_text())
	print("*****Description: " + subhead.get_text() + "\n\n")

