#!/usr/bin/env python

from __future__ import division
from Quad import Quad

class Card(Quad):
   def __init__(self, texture, height):
      Quad.__init__(self, texture)
      # Natural resolution of cards is 480x680
      cardAspect = 480/680
      self.height = height
      self.width = self.height * cardAspect
