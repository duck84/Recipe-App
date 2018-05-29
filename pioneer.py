from bs4 import BeautifulSoup
import requests
import pickle
from multiprocessing.dummy import Pool as ThreadPool
import itertools
from collections import defaultdict

recipes = defaultdict(list)
to_scrap = set()
scrapped = set()
links = set()

try:
    with open('database.pkl', 'rb') as fp:
        recipes = pickle.load(fp)
except:
    pass

def search(soup):
    ingredients = []
    try:
        recipe = soup.title.text
    except AttributeError:
        return
    for i in soup.find_all('span', {'itemprop' : 'name'}):
        if i.text in ingredients:
            continue
        ingredients.append(i.text)
    return recipe, ingredients

def searcher(site="", total= 2500):                       
    root = 'thepioneerwoman.com'
    skip = ['jpg', 'comment', 'facebook']
    to_scrap.add(site)
    while len(to_scrap) and len(recipes) <= total:
        try:
            scrapping = to_scrap.pop()
            if scrapping in scrapped or skip[0] in scrapping or skip[1] in scrapping or skip[2] in scrapping:
                continue
            scrapped.add(scrapping)
            connection = requests.get(scrapping)
        except requests.exceptions.MissingSchema:
            continue
        except requests.exceptions.InvalidSchema:
            continue
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            continue
        except TypeError:
            continue  
#        print("Scrapping {}".format(scrapping))
        soup = BeautifulSoup(connection.text, 'lxml')
        for link in soup.find_all('a'):
            if link.has_attr('href'):
                link = link['href']
                if link in links or skip[0] in link or skip[1] in link:
                    continue
                if root in link:
                    to_scrap.add(link)
                    if soup.find_all('ul', {'class': 'list-ingredients'}):
                        links.add(link)
                        x,y = (search(soup))
                        if x not in recipes:
                            recipes[x].append(link)
                            for y in y:
                                recipes[x].append(y)
        print("Recipes: {}    To Scrap: {}".format(len(recipes), len(to_scrap)))
    print("done")
    return links
    
searcher('http://thepioneerwoman.com/cooking_cat/all-pw-recipes/', 2152)
pool = ThreadPool(50)
stuff = pool.map(searcher, range(0, 50))
pool.close()
pool.join()

with open('database.pkl', 'wb') as fp:
    pickle.dump(recipes, fp)

x = 0
for key in recipes:
    print(key)
    x += 1
    try:
        for value in recipes[key]:
            print ("   {}".format(value))
    except:
        continue
    print(x)

