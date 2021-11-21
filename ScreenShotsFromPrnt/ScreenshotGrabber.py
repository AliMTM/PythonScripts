import requests
from bs4 import BeautifulSoup
import string
import random
import time
import os


def random_url():
    pool_s = string.ascii_letters
    pool_d = string.digits

    name = ''.join(random.choices(pool_s, k=2)) + ''.join(random.choices(pool_d, k=4))

    return name, requests.get(f"https://prnt.sc/{name}", headers={'User-Agent': 'Chrome'}).text


def img_grabber(img):
    if img:

        img = img['src']

        if img == '//st.prntscr.com/2021/10/22/2139/img/0_173a7b_211be8ff.png':
            print(f'{name} is trash')
            return

        if img[:len('https:')] == 'https:':
            img = requests.get(img, headers={'User-Agent': 'Chrome'})

        else:
            img = requests.get('https:' + img)

        return img


if __name__ == '__main__':

    for i in range(50):

        name, html = random_url()

        soup = BeautifulSoup(html, 'lxml')

        img = img_grabber(soup.find(id='screenshot-image'))

        if img:

            with open(f'img/{name}.png', 'wb') as f:
                f.write(img.content)

        else:
            print(f"{name} Not found")
