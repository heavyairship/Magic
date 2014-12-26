from __future__ import division
from Context import Context
from Texture import Texture
from Card import Card
import copy

def run():
   global context
   context = Context() 
   context.run() 

def drawBoard(player, y):
   pass

def drawHand(player):
   global context
   handSpacing = .25 # .25 "card heights" between each card
   total = len(player.hand)
   for i,card in enumerate(player.hand):
      # FixMe: Use the card's image name
      quad = Card(Texture.fromCache('Images/Sen Triplets.jpg'), .8)
      quad.x = (i - (total-1)/2) * .25
      quad.y = .5
      context.quad.append(quad)

def draw(game):
   global context
   context.quad = []

   player1 = game.currentPlayer
   player2 = game.defender()

   drawBoard(player1, -1)
   drawBoard(player2, 1)
   drawHand(player1)

def update(game):
   game = copy.deepcopy(game) 
   context.queue.put(lambda: draw(game))

