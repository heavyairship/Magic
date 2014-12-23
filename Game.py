from Player import Player

class Game(object):
   def __init__(self):
      self.players = [Player("Matt"),Player("Andrew")]
      self.currentPlayer = None
      self.attackers = []
      self.blockers = {}
      self.round = 0

   def defender(self):
      for player in self.players:
         if player!=self.currentPlayer:
            return player
