import requests
from bs4 import BeautifulSoup
import pprint
import sys


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 100:
                hn.append({'title': title, 'link': href, 'score': points})
    return hn


def get_hn_data(urls):
    hn = []
    for url in urls:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titlelink')
        subtext = soup.select('.subtext')
        hn.extend(create_custom_hn(links, subtext))
    return sorted(hn, key=lambda link: link['score'], reverse=True)


def main():
    up_to_page = int(input('how many pages to organize? '))
    base_link = 'https://news.ycombinator.com/news?p='
    pages = []
    for page in range(up_to_page):
        pages.append(base_link + str(page + 1))

    pprint.pprint(get_hn_data(pages))


if __name__ == '__main__':
    sys.exit(main())
