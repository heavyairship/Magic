from Card import Card

INITIAL_PLAYER_LIFE = 20

class Player(object):
  def __init__(self,name):
      self.name = name
      self.library = []
      self.hand = []
      self.board = []
      self.graveyard = []
      self.life = INITIAL_PLAYER_LIFE
       
