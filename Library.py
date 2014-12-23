import json 
from Card import Card

def load(path):
   f = open(path)
   libJson = json.loads(f.read())
   library = []
   for c in libJson:
      library.append(Card(c))
   return library
