import requests
from bs4 import BeautifulSoup

def crawl_news():
    url = "https://investing.com/news/stock-market-news"

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    news_list = soup.select('a[data-test="article-title-link"]')

    news_data = []
    for news in news_list:
        title = news.get_text(strip=True)
        link = news['href']

        thumbnail_tag = news.find_previous_sibling('img')
        thumbnail_url = thumbnail_tag['src[item-image]'] if thumbnail_tag else None

        news_data.append({
            'title': title,
            'link': link,
            'thumbnail': thumbnail_url
        })

    return news_data

news_data = crawl_news()
for idx, news in enumerate(news_data, 1):
    print(f"{idx}. {news['title']}\n   Link: {news['link']}\n   Thumbnail: {news['thumbnail']}")