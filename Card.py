import copy

# List of attributes in a Card

CARD_ATTRS = [
   "name",
   "manaCost",
   "cmc",
   "colors",
   "type",
   "supertypes",
   "types",
   "subtypes",
   "rarity",
   "text",
   "flavor",
   "artist",
   "number",
   "power",
   "toughness",
   "layout",
   "multiverseid",
   "imageName"
]


class Card(object):
   def __init__(self,json):
      self.name = json["name"]
      self.manaCost = json["manaCost"]
      self.cmc = json["cmc"]
      self.colors = json["colors"]
      self.type = json["type"]
      self.supertypes = json["supertypes"]
      self.types = json["types"]
      self.subtypes = json["subtypes"]
      self.rarity = json["rarity"]
      self.text = json["text"]
      self.flavor = json["flavor"]
      self.artist = json["artist"]
      self.number = json["number"]
      self.power = int(json["power"])
      self.toughness = int(json["toughness"])
      self.layout = json["layout"]
      self.multiverseid = json["multiverseid"]
      self.imageName = json["imageName"]

   
