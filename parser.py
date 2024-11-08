import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as Bs
from curl_cffi.requests import Session


class QuotesParser:
    user_agent = UserAgent().random
    def __init__(self):
        self.__i = 1
        self.__pages = []
        self.__headers = {"User-Agent": QuotesParser.user_agent}
        self.base_url = "https://quotes.toscrape.com"
        self.__all_data = {}

    def get_count_pages(self):
        page = 1
        with Session(headers=self.__headers) as curl:
            while True:
                url = f"https://quotes.toscrape.com/page/{page}/"
                html = curl.get(url)
                soup = Bs(html.text, 'lxml')
                quotes = soup.find_all(name='div', class_='quote')
                if quotes:
                    self.__pages.append(html.text)
                    page += 1
                else:
                    return self.__pages

    def parse_all_page(self):
        for page in self.__pages:
            soup = Bs(page, 'lxml')
            quotes = soup.find_all(name='div', class_='quote')

            for q in quotes:
                text = q.find('span', class_='text').text.replace('"', "'")
                author = q.find('small', class_='author')
                link_author = author.find_next_sibling("a")['href']
                tags = {}
                tags_el = q.find_all('a', class_='tag')
                for tag in tags_el:
                    tag_name = tag.text
                    tag_link = tag['href']
                    tags[tag_name] = self.base_url+tag_link

                self.__all_data[self.__i] = {
                    "text": text,
                    "author": author.text,
                    "link_author": self.base_url+link_author,
                    "tags": tags
                }
                self.__i += 1
        return self.__all_data

    def write_data_to_json(self):
        with open('quotes.json', 'w') as file:
            json.dump(self.__all_data, file, indent=2, ensure_ascii=False)

