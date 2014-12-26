import copy
import pdb
import sys
import time
import os
import Graphics

INITIAL_DRAW = 7
ENDC = '\033[0m' 
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
CYAN = '\033[96m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
GREY = '\033[90m'
BLACK = '\033[90m'
DEFAULT = '\033[99m'

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
      print RED+"%s loses!" % (player.name)+ENDC
      raise sys.exit(0)

def colorFor(player):
   if player.name=="Matt":
      return BLUE
   return YELLOW
      
def printBoard(game):
   for player in game.players:
      color = colorFor(player)
      print color+"%s's board (life=%d): " % (player.name,player.life)+ENDC
      for i,card in player.board.iteritems():
         action = ""
         if card in game.attackers.values():
            action = "(attacking)"
         elif card in game.blockers.values(): 
            action = "(blocking)"
         print "%d %s %d/%d %s" % (i,card.name,card.power,card.toughness,action)  
      print

###################
# Beginning Phase #
###################

def untapStep(game):
   for card in game.currentPlayer.board.itervalues():
      card.isTapped = False

def upkeepStep(game):
   pass

def drawCard(player):
   if len(player.hand)>=7:
      raise Exception("Cannot draw more than 7 cards")
         
   if len(player.library)==0:
      player.life = 0
      return
      
   (i,card) = player.library.iteritems().next()
   player.hand[i] = card
   del player.library[i]

def drawStep(game):
   player = game.currentPlayer
   if game.round==1:
      for i in range(INITIAL_DRAW):
         drawCard(player)
   else:
      try:
         drawCard(player)
      except Exception:
         print RED+"%s's hand is full, cannot draw!\n" % (player.name)+ENDC
         time.sleep(1)

def beginningPhase(game):
   clear()
   color = colorFor(game.currentPlayer)
   print color+"**** Beginning turn for %s ****\n" % (game.currentPlayer.name)+ENDC
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
   Graphics.update(game)
   printBoard(game)
   player = game.currentPlayer
   print GREEN+"Here is your hand: "+ENDC
   for i,card in player.hand.iteritems():
      print "%d %s %d/%d" % (i,card.name,card.power,card.toughness)
   print  

   prompt = "%s, choose cards to play (or hit enter for none): " % player.name
   color = colorFor(player)
   inp = raw_input(color+prompt+ENDC)
   inp = inp.split()
   inp = [int(i) for i in inp]
   for i in inp:
      card = player.hand[i]
      player.board[i] = card
      del player.hand[i]
   Graphics.update(game)

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
   prompt = "%s, choose attackers (or hit enter for none): " % player.name
   color = colorFor(player)
   inp = raw_input(color+prompt+ENDC)
   inp = inp.split()
   inp = [int(i) for i in inp]
   for i in inp:
      game.attackers[i] = player.board[i]

def declareBlockers(game):
   if len(game.attackers)==0:
      return
   clear()
   printBoard(game)
   player = game.defender()
   prompt = "%s, choose blockers (list of <attacker-id>-<defender-id> " \
      "or hit enter for none): " % player.name
   color = colorFor(player)
   inp = raw_input(color+prompt+ENDC)
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
   for attacker in game.attackers.itervalues():
      if not attacker.isBlocked:
         player.life = player.life-attacker.power

def sendToGraveYard(cardList,graveyard,card):
   index = None 
   for i,c in cardList.iteritems():
      if c==card:
         index = i
         break
   c = cardList[index]
   graveyard[index] = c
   del cardList[index]
    
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

   game.attackers = {}
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
   print GREEN+"\n**********************"
   print "* Welcome, to Magic! *"
   print "**********************\n"+ENDC
   time.sleep(1)
   while True:
      game.round = game.round+1
      for p in game.players:
         game.currentPlayer = p
         doTurn(game)            
