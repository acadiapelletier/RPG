# Shows inventory if player inputs
# 'open inventory' action

import enemy as enemy
import game_map as game_map
inventory_list = []


def open_inventory():
  print(f"""\nWhat would you like to see?
Type 'quit' when finished: {inventory_list}""")

  prompt = 'ACTION: '

  while True:
    key = input(prompt)

    if key == 'mysterious book':
      enemy.show_enemies()
      game_map.show_gamemap()
    elif key == 'magic spellbook':
      print("""\nSpecial book of spells. This book
includes three spells that can be used at any
point. Spells available:
Flame Thrower: a spell that throws fire, doing 20 damage.
Special Attack: this spell is a mystery, it does 30 damage
Final Blow: it aims a powerful blow, it does 30 damage""")
    elif key == 'magic wand':
      print("""\nMagic wand, you can cast any spell you
learn.""")
    elif key == 'magic potion':
      print("""\nHealing potion that heals 30 damage.
Can only be used once.""")
    elif key == 'quit':
      break
    else:
      print("\nHuh? You can't do that right now.")
