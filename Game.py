from Player import Player

class Game(object):
   def _loadPlayerInfo():
      
   def __init__(self):
      self._players = _loadPlayerInfo()
      assert len(players)>1

   ###################
   # Beginning Phase #
   ###################

   def untapSetp():
      pass

   def upkeepStep():
      pass

   def drawStep():
      pass

   def beginningPhase():
      untapStep()
      upkeepStep()
      drawStep()

   ####################
   # First Main Phase #
   ####################

   def handleMainPhaseTriggers():
      pass

   def handleInstantsAndActivatedAbilities():
      pass

   def handleNonInstants():
      pass   

   def checkManaBurn():
      pass

   def firstMainPhase():
      handleMainPhaseTriggers()
      handleInstantsAndActivatedAbilities()
      handleNonInstants()
      checkManaBurn()

   ################
   # Combat Phase #
   ################

   def beginCombatStep():
      pass

   def declareAttackers()
      pass

   def declareBlockers()
      pass

   def combatDamageStep()
      pass
   
   def endOfCombatStep()
      pass

   def combatPhase():
      beginCombatStep()
      declareAttackers()
      declareBlockers()
      combatDamageStep()
      endOfCombatStep()

   #####################
   # Second Main Phase #
   #####################

   def handleSecondMainPhaseTriggers():
      pass

   def secondMainPhase():
      handleSecondMainPhaseTriggers()
      handleInstantsAndActivatedAbilities()
      handleNonInstants()
      checkManaBurn()

   #############
   # End Phase #
   #############

   def endOfTurnStep():
      pass
   
   def cleanupStep():
      pass

   def endPhase():
      endOfTurnStep()
      cleanupStep()

   def doTurn():
      beginningPhase()
      firstMainPhase()
      combatPhase()
      secondMainPhase()
      endPhase()   

   def run(self):
      while True:
         for p in self._players:
            self._currentPlayer = p
            doTurn()            
