import copy
from TypeCheckUtil import checkType

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
      if not len(CARD_ATTRS)==len(json):
         raise ValueError("JSON object is missing attrs")
      # Validate json size

      for a in CARD_ATTRS:
         v = json[a]

         if a in ["colors","supertypes","types","subtypes"]:
            checkType(v,list)
            for e in v:
               checkType(e,str)
         # Validate list attrs

         elif a in ["cmc","multiverseid"]:
            checkType(v,int)
         # Validate int attrs 

         else:
            checkType(v,str)
         # Validate string attrs

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
      checkType(immutableCard,ImmutableCard)
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
      checkType(value,str)
      self._data["name"] = value

   @manaCost.setter
   def manaCost(self,value):
      checkType(value,str)
      self._data["manaCost"] = value

   @cmc.setter
   def cmc(self,value):
      checkType(value,int)
      self._data["cmc"] = value

   @colors.setter
   def colors(self,value):
      checkType(value,list)
      for e in value:
         checkType(e,str)
      self._data["colors"] = copy.deepcopy(value)

   @type.setter
   def type(self,value):
      checkType(value,str)
      self._data["type"] = value

   @supertypes.setter
   def supertypes(self,value):
      checkType(value,list)
      for e in value:
         checkType(e,str)
      self._data["supertypes"] = copy.deepcopy(value)

   @types.setter
   def types(self,value):
      checkType(value,list)
      for e in value:
         checkType(e,str)
      self._data["types"] = copy.deepcopy(value)

   @subtypes.setter
   def subtypes(self,value):
      checkType(value,list)
      for e in value:
         checkType(e,str)
      self._data["subtypes"] = copy.deepcopy(value)

   @rarity.setter
   def rarity(self,value):
      checkType(value,str)
      self._data["rarity"] = value

   @text.setter
   def text(self,value):
      checkType(value,str)
      self._data["text"] = value

   @flavor.setter
   def flavor(self,value):
      checkType(value,str)
      self._data["flavor"] = value

   @artist.setter
   def artist(self,value):
      checkType(value,str)
      self._data["artist"] = value

   @number.setter
   def number(self,value):
      checkType(value,str)
      self._data["number"] = value

   @power.setter
   def power(self,value):
      checkType(value,int)
      self._data["power"] = value

   @toughness.setter
   def toughness(self,value):
      checkType(value,int)
      self._data["toughness"] = value

   @layout.setter
   def layout(self,value):
      checkType(value,str)
      self._data["layout"] = value

   @multiverseid.setter
   def multiverseid(self,value):
      checkType(value,int)
      self._data["multiverseid"] = value

   @imageName.setter
   def imageName(self,value):
      checkType(value,str)
      self._data["imageName"] = value

# End Card class
   
