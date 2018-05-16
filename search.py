from collections import defaultdict
from bs4 import BeautifulSoup
import pickle
import requests
from multiprocessing.dummy import Pool as ThreadPool

recipes = defaultdict(list)
fp = open('database.pkl', 'rb')
data = pickle.load(fp)

#with open("test.html") as fp:
def search(test=0):
     while(data):
        try:
            print(len(data))
            x = requests.get(data.pop())
            soup = BeautifulSoup(x.text, 'lxml')           
        except requests.exceptions.MissingSchema:
            continue
        except requests.exceptions.InvalidSchema:
            continue
        except requests.exceptions.ReadTimeout:
            continue
        try:
            recipe = soup.title.text
        except AttributeError:
            continue
        for ultag in soup.find_all('ul', {'class': 'wprm-recipe-ingredients'}):
            for litag in ultag.find_all('li', {'class': 'wprm-recipe-ingredient'}):
                for i in litag.find_all('span', {'class': 'wprm-recipe-ingredient-name'}):
                   recipes[recipe].append(i.text)
fp.close()

pool = ThreadPool(30)
stuff = pool.map(search, range(0,30))
pool.close()
pool.join()

f = open('recipes.pkl', 'wb')
pickle.dump(recipes, f)
f.close()   


x = 0
for key in recipes:
    print(key)
    x += 1
    try:
        for value in recipes[key]:
            print ('   ', value)
    except:
        continue
    print(x)
#print(recipes.items())
