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

def search(soup):
    ingredients = []
    try:
        recipe = soup.title.text
    except AttributeError:
        return
        for i in soup.find_all('li', {'class' : 'jetpack-recipe-ingredient'}):
            ingredients.append(i.text)
        return recipe, ingredients 

def searcher(site="", total=1000):                       
    root = 'smittenkitchen.com'
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
                    if soup.find_all('li', {'class': 'jetpack-recipe-ingredients'}):
                        links.add(link)
                        x,y = (search(soup))
                        if x not in recipes:
                            for y in y:
                                recipes[x].append(y)
        print("Recipes: {}    To Scrap: {}".format(len(recipes), len(to_scrap)))
    print("done")
    return links

#to_scrap.add('http://smittenkitchen.com/recipes')   
searcher('https://smittenkitchen.com/2006/09/silky-cauliflower-soup/', 1) 
#searcher('http://smittenkitchen.com/recipes', 0)
pool = ThreadPool(30)
stuff = pool.map(searcher, range(0, 30))
pool.close()
pool.join()

#f = open('database.pkl', 'wb')
#pickle.dump(recipes, f)
#f.close

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
