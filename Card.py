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
      self.name = json.get("name")
      self.manaCost = json.get("manaCost")
      self.cmc = json.get("cmc")
      self.colors = json.get("colors")
      self.type = json.get("type")
      self.supertypes = json.get("supertypes")
      self.types = json.get("types")
      self.subtypes = json.get("subtypes")
      self.rarity = json.get("rarity")
      self.text = json.get("text")
      self.flavor = json.get("flavor")
      self.artist = json.get("artist")
      self.number = json.get("number")
      self.power = int(json.get("power"))
      self.toughness = int(json.get("toughness"))
      self.layout = json.get("layout")
      self.multiverseid = json.get("multiverseid")
      self.imageName = json.get("imageName")

      self.isTapped = False
      self.isBlocked = False
      self.hasSummoningSickness = True
