## Prelease version

## Character info of the player
player_info = {'name' : 'Barnabas' , 'age' : '20' , 'secret' : 'You were kidnapped because of your secret abilities'}
## Prints the info above
for title, info in player_info.items():
  print(f"This character's {title}: {info}.")
print("")

## Character info of oaf
oaf_info = {'name' : 'King Bulbin' , 'traits' : ['Craves power' , 'Smelly' , 'Anger issues'] , 'fighting information' : 'Hits hard but moves slow'}
## Prints the info above
for title, info in oaf_info.items():
  print(f"This character's {title}: {info}.")
print("")

## Character info of the elves
elves_info = {'name' : "They don't have names" , 'traits' : ['Loyal to the king' , 'Live to serve the king' , "They don't talk"] , 'fighting information' : 'Attacks do less damage but move quicker.'}
## Prints the info above
for title, info in elves_info.items():
  print(f"This character's {title}: {info}")
print("")

## Descriptions of dungeon player starts in
dungeon = {'physical description' : ['dingy' , 'dark' , 'damp' , 'pungent odor'] , 'What you see' : ['cell bars and door that keep you locked in' , 'a key hanging outside of the cell door' , 'a bed and toilet' , 'a loose cell bar']}
## Prints the info above
for title, info in dungeon.items():
  description = f"{dungeon['physical description']}"
  items_to_find = f"{dungeon['What you see']}"

  print(f"You find yourself in a {description} room. What you see is {items_to_find}")
print("")

## Description of the room the player is in after they leave the dungeon
first_room = {'What you see' : ['a magic potion' , 'two hallways']}
## Prints the info above
for title, info in first_room.items():
  print(f"You leave the dungeon and enter another room, you look around and see {info}.")
print("")

## Description of the next room the player is in
second_room = {'What you see' : ['Book of Spells' , 'Magic Wand']}
## Prints the info above
for info in second_room.values():
  print(f"You took the right turn! You now find yourself in another room, you look around and see {info}.")
print("")

## Description of rooms you go into when you take a wrong turn
bad_rooms = {'What you see' : 'Elves standing, ready to fight'}
## Prints the info above
for info in bad_rooms.values():
  print(f"Uh-oh! You must have taken a wrong turn! You look ahead and see {info}.")
print('')

## Description of the items
items = {'Magic Wand' : 'a wand that will complete any spells you ask it to do.' , 'Book of Spells' : 'a book that carries spells to use, although each spell can only be used once' , 'Key' : 'a small key that unlocks any door in your area' , 'Healing potion' : 'a potion that heals 20 damage'}
## Prints info above
for item, description in items.items():
  print(f"This item is a {item}, it is {description}.")
print("")

## Description of the spells
spells = {'Flame Thrower' : 'it throws fire, doing 20 damage to an opponent' , 'Special Attack' : 'it is a mystery, it does 30 damage to an opponent' , 'Final Blow' : 'it aims a powerful blow at the chest, it does 30 damage to an opponent'}
## Prints info above
for item, description in spells.items():
  print(f"This spells is called {item}, {description}")
