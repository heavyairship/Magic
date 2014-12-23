import json 
from Card import Card

def load(path):
   f = open(path)
   libJson = json.loads(f.read())
   library = {}
   for i,c in enumerate(libJson):
      library[i] = Card(c)
   return library
