from collections import defaultdict

def search(soup):
    ingredients = []
    try:
        recipe = soup.title.text
    except AttributeError:
        return
    for ultag in soup.find_all('ul', {'class': 'wprm-recipe-ingredients'}):
        for litag in ultag.find_all('li', {'class': 'wprm-recipe-ingredient'}):
            for i in litag.find_all('span', {'class': 'wprm-recipe-ingredient-name'}):
               ingredients.append(i.text)
    return recipe, ingredients
