from collections import defaultdict
from bs4 import BeautifulSoup
import pickle
from urllib.request import urlopen

recipes = defaultdict(list)

#with open("test.html") as fp:
with open('database.pkl', 'rb') as fp:
    data = pickle.load(fp)
    for connection in data:
        x = connection.geturl()
        soup = BeautifulSoup(urlopen(x), 'lxml')
        recipe = soup.title.text
        for ultag in soup.find_all('ul', {'class': 'wprm-recipe-ingredients'}):
            for litag in ultag.find_all('li', {'class': 'wprm-recipe-ingredient'}):
                for i in litag.find_all('span', {'class': 'wprm-recipe-ingredient-name'}):
                    recipes[recipe].append(i.text)
fp.close()

f = open('recipes.pkl', 'wb')
pickle.dump(recipes, f)
f.close()
        

for key in recipes:
    print(key)
    for value in recipes[key]:
        print ('   ', value)
#print(recipes.items())
