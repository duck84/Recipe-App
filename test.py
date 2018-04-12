import pickle

with open('recipes.pkl', 'rb') as fp:
    data = pickle.load(fp)

for key in data:
    if 'blueberries' in data[key]:
        print (key)

