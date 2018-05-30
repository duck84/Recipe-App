from bs4 import BeautifulSoup
import requests
import pickle
from multiprocessing.dummy import Pool as ThreadPool
import itertools
from collections import defaultdict
import os

os.chdir('/u/mmcgrath/Spring/Project/Databases')
recipes = defaultdict(list)
to_scrap = set()
scrapped = set()
links = set()

try:
    with open('thegoods.pkl', 'rb') as fp:
        recipes = pickle.load(fp)
except:
    pass

def search(soup):
    ingredients = []
    try:
        recipe = soup.title.text
    except AttributeError:
        return
    if soup.find_all('ul', {'class':'wprm-recipe-ingredients'}): 
#        ultag = soup.find('ul', {'class': 'wprm-recipe-ingredients'})
#        for litag in ultag.find_all('li', {'class': 'wprm-recipe-ingredient'}):
#             i = litag.find('span', {'class': 'wprm-recipe-ingredient-name'})
        for i in soup.find_all('span', {'class' : 'wprm-recipe-ingredient-name'}):
            ingredients.append(i.text)
        return recipe, ingredients
    else:
#        for ultag in soup.find_all('ol', {'class': 'blog-yumprint-ingredients'}):
            for litag in soup.find_all('li', {'class': 'blog-yumprint-ingredient-item'}):
#                for i in litag.find_all('span', {'class': 'wprm-recipe-ingredient-name'}):
                text = litag.text
                if "-" in text:
                    text = text[0:text.index('-') - 1]
                ingredients.append(text)
            return recipe, ingredients       

def searcher(site="", total=1000):                       
    root = 'bakingthegoods.com'
    skip = ['jpg', 'comment', 'tag']
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
                    if soup.find_all('ul', {'class': 'wprm-recipe-ingredients'}) or \
                        soup.find_all('ol', {'class': 'blog-yumprint-ingredients'}):
                        links.add(link)
                        x,y = (search(soup))
                        if x not in recipes:
                            recipes[x].append(link)
                            for y in y:
                                recipes[x].append(y)
        print("Recipes: {}    To Scrap: {}".format(len(recipes), len(to_scrap)))
    print("done")
    return links
    
searcher('http://bakingthegoods.com/recipes', 100)
pool = ThreadPool(50)
stuff = pool.map(searcher, range(0, 50))
pool.close()
pool.join()

with open('thegoods.pkl', 'wb') as fp:
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

