import pickle
from collections import defaultdict

master = defaultdict(list)
with open('andiemitchell.pkl', 'rb') as f:
    master.update(pickle.load(f))
with open('lebovitz.pkl', 'rb') as f:
    master.update(pickle.load(f))
with open('pioneer.pkl', 'rb') as f:
    master.update(pickle.load(f))
with open('thegoods.pkl', 'rb') as f:
    master.update(pickle.load(f))
with open('bonappetit.pkl', 'rb') as f:
    master.update(pickle.load(f))
with open('orangette.pkl', 'rb') as f:
    master.update(pickle.load(f))
with open('serious.pkl', 'rb') as f:
    master.update(pickle.load(f))
with open('whiteonrice.pkl', 'rb') as f:
    master.update(pickle.load(f))

with open('master.pkl', 'wb') as f:
    pickle.dump(master, f)


for key in sorted(master):
    print(key)
print(len(master))
