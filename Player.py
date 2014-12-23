from Card import Card
from Library import load

INITIAL_PLAYER_LIFE = 20

class Player(object):
  def __init__(self,name):
      self.name = name
      if name=="Matt":
         self.library = load("testLibrary.json")
      else: 
         self.library = load("testLibrary2.json")
      self.hand = []
      self.board = []
      self.graveyard = []
      self.life = INITIAL_PLAYER_LIFE
      self.manaPool = {
         "black" : 0,
         "white" : 0,
         "blue" : 0,
         "red" : 0,
         "green" : 0,
         "colorless" : 0
      }

       
