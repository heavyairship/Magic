from Card import Card,ImmutableCard
from TypeCheckUtil import checkType

class CardList(tuple):
   def __new__(cls):
      return tuple.__new__(cls,(list(),))
   
   def add(self,c):
      checkType(c,Card)
      self[0].append(c)

   def remove(self,c):
      self[0].remove(c)

   def __iter__(self):
      return iter(self[0])
