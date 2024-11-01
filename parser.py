from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
from curl_cffi import requests


class QuotesParser:
    user_agent = UserAgent().random
    def __init__(self):
        self.__i = 1
        self.__headers = {"User-Agent": QuotesParser.user_agent}
        self.base_url = "https://quotes.toscrape.com/"
        self.__all_data = {}

    def parse_page(self, url):
        html = requests.get(url=url, headers=self.__headers).text
        soup = bs(html, 'lxml')
        quotes = soup.find_all(name='div', class_='quote')

        for q in quotes:
            text = q.find('span', class_='text').text
            author = q.find('small', class_='author').text
            tags = {}
            tags_el = q.find_all('a', class_='tag')
            for tag in tags_el:
                tag_name = tag.text
                tag_link = tag['href']
                tags[tag_name] = tag_link

            self.__all_data[self.__i] = {
                "text": text,
                "author": author,
                "tags": tags
            }
        return soup

    def get_all_data(self):
        soup = self.parse_page(self.base_url)
        print("get 1 page")
        next_page = soup.find(name='ul', class_='pager').find(name='li', class_='next')

        page = 2
        while next_page:
            url = f"https://quotes.toscrape.com/page/{page}/"
            self.parse_page(url)
            print(f"get {page} page")
            page += 1
            next_page = soup.find(name='ul', class_='pager').find(name='li', class_='next')

        print("Cancel")


parser = QuotesParser()
parser.get_all_data()
pass
