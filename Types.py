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

# Begin Card class 

class Card(tuple):
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

	def __new__(cls,json):
		Card._validate(json)
		return tuple.__new__(cls,(copy.deepcopy(json),))

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
	def rartity(self):
		return self[0]["rartity"]

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

c = Card(testJson)
print c.name
print c.multiverseid
