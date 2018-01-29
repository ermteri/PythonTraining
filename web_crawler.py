import requests
from bs4 import BeautifulSoup
import urllib
import time

def continue_crawl(history, target):
    if history[-1] == target:
        print("Target found!")
        return False
    elif len(history) > 25:
        print("Max jumps reached!")
        return False
    elif history[-1] in history[:-1]:
        print("We are looping")
        return False
    else:
        return True

def find_first_link(url):
    first_relative_link = None
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    content_div = soup.find(id='mw-content-text').find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=True):
        if element.find("a", recursive=False):
            first_relative_link = element.find("a", recursive=False).get('href')
            break
    if not first_relative_link:
        return
    return urllib.parse.urljoin('https://en.wikipedia.org/', first_relative_link )


start_url = 'https://en.wikipedia.org/wiki/Ludwig_van_Beethoven'
#start_url = 'https://en.wikipedia.org/wiki/Special:Random'
#start_url = "https://en.wikipedia.org/wiki/Russian_language"
target_url = 'https://en.wikipedia.org/wiki/Philosophy'
article_chain = [start_url]
while continue_crawl(article_chain, target_url):
    first_link = find_first_link(article_chain[-1])
    print(first_link)
    if not first_link:
        print("We've arrived at a page w/o links, aborting")
        break
    article_chain.append(first_link)
    time.sleep(2)

