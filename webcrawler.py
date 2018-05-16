from bs4 import BeautifulSoup
import urllib.request
import pickle

links = []
checked = []
to_scrap = []

connection = urllib.request.urlopen('http://bakingthegoods.com/recipes/')
soup = BeautifulSoup(connection, 'lxml')

for link in soup.find_all('a'):
    if link.get('href') in links:
        continue
    links.append(link.get('href'))

count = 0
for l in links:
    try:
        if 'http://bakingthegoods.com' in l and count < 1000:
            print("Processing: ", l, count)
            connection = urllib.request.urlopen(l)
            if connection in checked:
                links.remove(l)
                continue
            stew = BeautifulSoup(connection, 'lxml')
            if stew.find_all('ul', {'class': 'wprm-recipe-ingredients'}) or \
               stew.find_all('ol', {'class': 'blog-yumprint-ingredients'}):
                print('HIT')
                to_scrap.append(connection)   
                count += 1
            checked.append(connection)
    except urllib.error.HTTPError:
        continue

f = open('database.pkl', 'wb')
pickle.dump(to_scrap, f)
f.close


