from Card import Card
 
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
assert c.name=="Sen Triplets"
assert c.imageName=="sen triplets"

