from Library import Library
from Hand import Hand
from Board import Board
from Graveyard import Graveyard
from TypeCheckUtil import checkType

INITIAL_PLAYER_LIFE = 20

class Player(object):
  def __init__(self,name):
      self._name = name
      self._library = Library()
      self._hand = Hand()
      self._board = Board()
      self._graveyard = Graveyard()
      self._life = INITIAL_PLAYER_LIFE
       
