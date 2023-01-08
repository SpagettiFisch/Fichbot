from twill.commands import *
from bs4 import BeautifulSoup
import re
import time
start = time.perf_counter()

def get_file():
    go('https://www.leagueoflegends.com/de-de/news/tags/patch-notes/')
    with open('index.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    go((soup.find_all('a', href=True))[0]['href'])
get_file()

print(f'The operation took about {round(time.perf_counter() - start, 4)}s')