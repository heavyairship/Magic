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

class ImmutableCard(tuple):
   @staticmethod
   def _validate(json):
      assert len(CARD_ATTRS)==len(json)
      for a in CARD_ATTRS:
         assert a in json
         v = json[a]
         if a in ["colors","supertypes","types","subtypes"]:
            assert isinstance(v,list)
            for e in v:
               assert isinstance(e,str)      
         elif a in ["cmc","multiverseid"]:
            assert isinstance(v,int)
         else:
            assert isinstance(v,str)

   @staticmethod
   def _powerToughnessToInt(json):
      json["power"] = int(json["power"])
      json["toughness"] = int(json["toughness"])
      
   def __new__(cls,json_):
      json = copy.deepcopy(json_)
      ImmutableCard._validate(json)
      ImmutableCard._powerToughnessToInt(json)
      return tuple.__new__(cls,(json,))

   # Accessors 

   @property
   def name(self):
      return self[0]["name"]

   @property
   def manaCost(self):
      return self[0]["manaCost"]

   @property
   def cmc(self):
      return self[0]["cmc"]

   @property
   def colors(self):
      return copy.deepcopy(self[0]["colors"])

   @property
   def type(self):
      return self[0]["type"]

   @property
   def supertypes(self):
      return copy.deepcopy(self[0]["supertypes"])

   @property
   def types(self):
      return copy.deepcopy(self[0]["types"])

   @property
   def subtypes(self):
      return copy.deepcopy(self[0]["subtypes"])

   @property
   def rarity(self):
      return self[0]["rarity"]

   @property
   def text(self):
      return self[0]["text"]

   @property
   def flavor(self):
      return self[0]["flavor"]

   @property
   def artist(self):
      return self[0]["artist"]

   @property
   def number(self):
      return self[0]["number"]

   @property
   def power(self):
      return self[0]["power"]

   @property
   def toughness(self):
      return self[0]["toughness"]

   @property
   def layout(self):
      return self[0]["layout"]

   @property
   def multiverseid(self):
      return self[0]["multiverseid"]

   @property
   def imageName(self):
      return self[0]["imageName"]

# End ImmutableCard class

class Card(object):
   def __init__(self,immutableCard):
      assert isinstance(immutableCard,ImmutableCard)
      self._data = copy.deepcopy(immutableCard[0])

   # Accessors 

   @property
   def name(self):
      return self._data["name"]

   @property
   def manaCost(self):
      return self._data["manaCost"]

   @property
   def cmc(self):
      return self._data["cmc"]

   @property
   def colors(self):
      return copy.deepcopy(self._data["colors"])

   @property
   def type(self):
      return self._data["type"]

   @property
   def supertypes(self):
      return copy.deepcopy(self._data["supertypes"])

   @property
   def types(self):
      return copy.deepcopy(self._data["types"])

   @property
   def subtypes(self):
      return copy.deepcopy(self._data["subtypes"])

   @property
   def rarity(self):
      return self._data["rarity"]

   @property
   def text(self):
      return self._data["text"]

   @property
   def flavor(self):
      return self._data["flavor"]

   @property
   def artist(self):
      return self._data["artist"]

   @property
   def number(self):
      return self._data["number"]

   @property
   def power(self):
      return self._data["power"]

   @property
   def toughness(self):
      return self._data["toughness"]

   @property
   def layout(self):
      return self._data["layout"]

   @property
   def multiverseid(self):
      return self._data["multiverseid"]

   @property
   def imageName(self):
      return self._data["imageName"]

   # Mutators

   @name.setter
   def name(self,value):
      assert isinstance(value,str)
      self._data["name"] = value

   @manaCost.setter
   def manaCost(self,value):
      assert isinstance(value,str)
      self._data["manaCost"] = value

   @cmc.setter
   def cmc(self,value):
      assert isinstance(value,int)
      self._data["cmc"] = value

   @colors.setter
   def colors(self,value):
      assert isinstance(value,list)
      for e in value:
         assert isinstance(e,str)
      self._data["colors"] = copy.deepcopy(value)

   @type.setter
   def type(self,value):
      assert isinstance(value,str)
      self._data["type"] = value

   @supertypes.setter
   def supertypes(self,value):
      assert isinstance(value,list)
      for e in value:
         assert isinstance(e,str)
      self._data["supertypes"] = copy.deepcopy(value)

   @types.setter
   def types(self,value):
      assert isinstance(value,list)
      for e in value:
         assert isinstance(e,str)
      self._data["types"] = copy.deepcopy(value)

   @subtypes.setter
   def subtypes(self,value):
      assert isinstance(value,list)
      for e in value:
         assert isinstance(e,str)
      self._data["subtypes"] = copy.deepcopy(value)

   @rarity.setter
   def rarity(self,value):
      assert isinstance(value,str)
      self._data["rarity"] = value

   @text.setter
   def text(self,value):
      assert isinstance(value,str)
      self._data["text"] = value

   @flavor.setter
   def flavor(self,value):
      assert isinstance(value,str)
      self._data["flavor"] = value

   @artist.setter
   def artist(self,value):
      assert isinstance(value,str)
      self._data["artist"] = value

   @number.setter
   def number(self,value):
      assert isinstance(value,str)
      self._data["number"] = value

   @power.setter
   def power(self,value):
      assert isinstance(value,int)
      self._data["power"] = value

   @toughness.setter
   def toughness(self,value):
      assert isinstance(value,int)
      self._data["toughness"] = value

   @layout.setter
   def layout(self,value):
      assert isinstance(value,str)
      self._data["layout"] = value

   @multiverseid.setter
   def multiverseid(self,value):
      assert isinstance(value,int)
      self._data["multiverseid"] = value

   @imageName.setter
   def imageName(self,value):
      assert isinstance(value,str)
      self._data["imageName"] = value

# End Card class
   
testJson = {
   "name" : "Sen Triplets",
   "manaCost" : "{2}{W}{U}{B}",
   "cmc" : 5,
   "colors" : ["White", "Blue", "Black"],
   "type" : "Legendary Artifact Creature - Human Wizard",
   "supertypes" : ["Legendary"],
   "types" : ["Artifact", "Creature"],
   "subtypes" : ["Human", "Wizard"],
   "rarity" : "Mythic Rare",
   "text" : ("At the beginning of your upkeep, choose target opponent."
      "This turn, that player can't cast spells or activate"
      "abilities and plays with his or her hand revealed."
      "You may play cards from that player's hand this turn."),
   "flavor" : "They are the masters of your mind.",
   "artist" : "Greg Staples",
   "number" : "109",
   "power" : "3",
   "toughness" : "3",
   "layout" : "normal",
   "multiverseid" : 180607,
   "imageName" : "sen triplets"
}

c = ImmutableCard(testJson)
assert c.name=="Sen Triplets"
assert c.multiverseid==180607

c2 = Card(c)
assert c2.name=="Sen Triplets"
c2.name = "Dingus Egg"
assert c2.name=="Dingus Egg"

assert c2.toughness==3
c2.toughness = c2.toughness-1
assert c2.toughness==2
