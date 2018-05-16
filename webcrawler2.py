from bs4 import BeautifulSoup
import requests
import pickle
from multiprocessing.dummy import Pool as ThreadPool
import itertools

# Checks webpage for recipe
def checker(link):
    connection = requests.get(link)
    stew = BeautifulSoup(connection.text, 'lxml')
    if stew.find_all('ul', {'class': 'wprm-recipe-ingredients'}) or \
         stew.find_all('ol', {'class': 'blog-yumprint-ingredients'}):
         return True;
    else:
        return False

def searcher(site, total):
    links = set()                                # links found
    to_scrap = set()                             # set still need to check
    scrapped = set()
    to_scrap.add(requests.get(site))
    while to_scrap and len(links) <= total:
        connection = to_scrap.pop()
        soup = BeautifulSoup(connection.text, 'lxml')
        for link in soup.find_all('a'):
            if link.has_attr('href'):
                link = link['href']
            else:
                continue
            if link in links or link in to_scrap:
                continue
            if site in link:
                try:
                    to_scrap.add(requests.get(link))
                    if checker(link):
                        links.add(link)
                        print(link)
                except requests.exceptions.MissingSchema:
                    continue
                except requests.exceptions.InvalidSchema:
                    continue
    print(len(links))
    return links

results = searcher('http://bakingthegoods.com', 5)
pool = ThreadPool(10)
urls = pool.map(searcher, zip(results, itertools.repeat(100, 10)))
pool.close()
pool.join()
print(urls)
print(len(urls))

#count = 0
#for l in links:
#    try:
#        if 'http://bakingthegoods.com' in l and count < 1000:
#            print("Processing: ", l, count)
#            connection = urllib.request.urlopen(l)
#            if connection in checked:
#                links.remove(l)
#                continue
#            stew = BeautifulSoup(connection, 'lxml')
#            if stew.find_all('ul', {'class': 'wprm-recipe-ingredients'}) or \
#               stew.find_all('ol', {'class': 'blog-yumprint-ingredients'}):
#                print('HIT')
#                to_scrap.append(connection)   
#                count += 1
#            checked.append(connection)
#    except urllib.error.HTTPError:
#        continue

#f = open('database.pkl', 'wb')
#pickle.dump(to_scrap, f)
#f.close


