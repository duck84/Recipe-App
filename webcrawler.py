from bs4 import BeautifulSoup
import urllib.request
import pickle

links = []
to_scrap = []

connection = urllib.request.urlopen('http://bakingthegoods.com/recipes/')
soup = BeautifulSoup(connection, 'lxml')

for link in soup.find_all('a'):
    links.append(link.get('href'))

count = 0
for l in links:
#    try:
        if 'http' in l and count < 100:
            print("Processing: ", l)
            connection = urllib.request.urlopen(l)
            stew = BeautifulSoup(connection, 'lxml')
            if stew.find_all('ul', {'class': 'wprm-recipe-ingredients'}):
                print('HIT')
                to_scrap.append(connection)   
                count += 1
#    except urllib.error.HTTPError:
#        continue

f = open('database.pkl', 'wb')
pickle.dump(to_scrap, f)
f.close


