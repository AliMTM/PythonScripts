import requests
from bs4 import BeautifulSoup
import os
import json

"""
This is a script to bring my favorite anime updates 
"""

PAGES = 5
MY_MANGA = ['Tales Of Demons And Gods', 'Solo Leveling', 'Sss-Class Suicide Hunter',
            'Return To Player', 'Ranker Who Lives A Second Time', 'My Wife Is A Demon Queen']


class Manganato:

    @staticmethod
    def pages():
        for i in range(1, PAGES + 1):
            yield requests.get(f'https://manganato.com/genre-all/{i}', headers={'User-Agent': 'Chrome'})

    @staticmethod
    def tags():
        for page in Manganato.pages():
            soup = BeautifulSoup(page.text, 'lxml')
            soup = soup.select('.genres-item-info')
            for e in soup:
                yield e

    @staticmethod
    def manga_extractor():
        for tag in Manganato.tags():
            yield {'manga_name': tag.h3.text,
                   'manga_last_chapter': tag.contents[3].text}


def make_json(mangas):
    if os.path.isfile('manga.json'):  # check if file_name.json is already exist

        with open('manga.json') as d:
            old_manga = json.load(d)  # load old data

        mangas = old_manga + mangas  # append the new data

    with open('manga.json', 'w') as outfile:
        json.dump(mangas, outfile)  # dump the new data


if __name__ == '__main__':

    mangas = [manga for manga in Manganato.manga_extractor() if manga['manga_name'] in MY_MANGA]

    make_json(mangas)
