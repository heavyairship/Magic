import copy
import pdb
import sys
import time
import os

INITIAL_DRAW = 7

###########
# Utility #
###########

def clear():
   os.system('cls' if os.name == 'nt' else 'clear')

def checkForEndGame(game):
   losers = []
   for player in game.players:
      if player.life<=0:
         losers.append(player)

   for loser in losers:
      print "player %s loses!" % player.name
      raise Exception("game over")

def printBoard(game):
   for player in game.players:
      print "%s's board (life=%d): " % (player.name,player.life)
      for i,card in enumerate(player.board):
         action = ""
         if card in game.attackers:
            action = "(attacking)"
         elif card in game.blockers: 
            action = "(blocking)"
         print "%d %s %d/%d %s" % (i,card.name,card.power,card.toughness,action)  
      print
      

###################
# Beginning Phase #
###################

def untapStep(game):
   for card in game.currentPlayer.board:
      card.isTapped = False

def upkeepStep(game):
   pass

def drawCard(player):
   if len(player.hand)>=7:
      raise Exception("Cannot draw more than 7 cards")
         
   if len(player.library)==0:
      player.life = 0
      return
      
   player.hand.append(player.library.pop(0))

def drawStep(game):
   player = game.currentPlayer
   if game.round==1:
      for i in range(INITIAL_DRAW):
         drawCard(player)
   else:
      drawCard(player)

def beginningPhase(game):
   clear()
   print "**** Beginning turn for %s ****\n" % game.currentPlayer.name
   untapStep(game)
   upkeepStep(game)
   drawStep(game)

####################
# First Main Phase #
####################

def handleMainPhaseTriggers(game):
   pass

def handleInstantsAndActivatedAbilities(game):
   pass

def handleNonInstants(game):
   printBoard(game)
   player = game.currentPlayer
   print "Here is your hand: "
   for i,card in enumerate(player.hand):
      print "%d %s %d/%d" % (i,card.name,card.power,card.toughness)
   print  

   inp = raw_input("Choose a card to play (or hit enter for none): ")
   # FixMe: support playing multiple cards
   inp = inp.split()
   for i in inp:
      player.board.append(player.hand.pop(int(i)))

def checkManaBurn(game):
   for player in game.players:
      damage = 0
      for count in player.manaPool.itervalues():
         damage = damage+count
      player.life = player.life-damage
   checkForEndGame(game)

def firstMainPhase(game):
   handleMainPhaseTriggers(game)
   handleInstantsAndActivatedAbilities(game)
   handleNonInstants(game)
   checkManaBurn(game)

################
# Combat Phase #
################

def beginCombatStep(game):
   pass

def declareAttackers(game):
   player = game.currentPlayer
   clear()
   printBoard(game)
   inp = raw_input("%s, choose attackers (or hit enter for none): " % player.name)
   game.attackers = [player.board[int(e)] for e in inp.split()]

def declareBlockers(game):
   if len(game.attackers)==0:
      return
   clear()
   printBoard(game)
   player = game.defender()
   inp = raw_input("%s, choose blockers (list of <attacker-id>-<defender-id> " 
      "or hit enter for none): " % player.name)
   inp = inp.split()
   for pair in inp:
      pair = pair.split("-")
      attackerId = int(pair[0])
      blockerId = int(pair[1])
      game.blockers[player.board[blockerId]] = game.attackers[attackerId]
      game.attackers[attackerId].isBlocked = True

def combatDamageStep(game):
   for blocker,attacker in game.blockers.iteritems():
      blocker.toughness = blocker.toughness-attacker.power
      attacker.toughness = attacker.toughness-blocker.power
   player = game.defender() 
   for attacker in game.attackers:
      if not attacker.isBlocked:
         player.life = player.life-attacker.power

def sendToGraveYard(cardList,graveyard,card):
   index = None 
   for i,c in enumerate(cardList):
      if c==card:
         index = i
         break
   graveyard.append(cardList.pop(index))
    
def endOfCombatStep(game):
   attackingBoard = game.currentPlayer.board
   attackingGraveyard = game.currentPlayer.graveyard
   defendingBoard= game.defender().board
   defendingGraveyard = game.defender().graveyard

   for blocker,attacker in game.blockers.iteritems():
      if blocker.toughness<=0:
         sendToGraveYard(defendingBoard,defendingGraveyard,blocker)
      if attacker.toughness<=0:
         sendToGraveYard(attackingBoard,attackingGraveyard,attacker)
   checkForEndGame(game)

   game.attackers = []
   game.blockers = {}

def combatPhase(game):
   beginCombatStep(game)
   declareAttackers(game)
   declareBlockers(game)
   combatDamageStep(game)
   endOfCombatStep(game)

#####################
# Second Main Phase #
#####################

def handleSecondMainPhaseTriggers(game):
   pass

def secondMainPhase(game):
   handleSecondMainPhaseTriggers(game)
   handleInstantsAndActivatedAbilities(game)
   handleNonInstants(game)
   checkManaBurn(game)

#############
# End Phase #
#############

def endOfTurnStep(game):
   pass

def cleanupStep(game):
   pass

def endPhase(game):
   endOfTurnStep(game)
   cleanupStep(game)

########
# Turn #
########

def doTurn(game):
   beginningPhase(game)
   firstMainPhase(game)
   combatPhase(game)
   #secondMainPhase(game)
   endPhase(game)   

#############
# Game Loop #
#############

def run(game):
   clear()
   print "\n**********************"
   print "* Welcome, to Magic! *"
   print "**********************\n"
   time.sleep(1)
   while True:
      game.round = game.round+1
      for p in game.players:
         game.currentPlayer = p
         doTurn(game)            
