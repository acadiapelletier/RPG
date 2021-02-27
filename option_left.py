# File for if the player chose to go left
import inventory as inv
import quit_game as qg
import end_of_game as eog

spells = ['flame thrower', 'special attack',
'final blow']

def option_left():
  # Player has to fight an elf
  print("""\nYou enter a room and oh no!
It seems you have run into one of the elves!
"You will not escape alive!" he yells.""")
  print("""Complete one of the following actions:
*open inventory \n*use spell \n*quit game""")

  prompt = 'ACTION: '

  while True:
    key = input(prompt)

    if key == 'open inventory':
      inv.open_inventory()
    elif key == 'use spell':
      print("You chose to use a spell!")
      break
    elif key == 'quit game':
      qg.quit_game()
    else:
      print("Huh? You can't do that here.")

  print("""\nUse a spell quickly!
The elf hit you, doing 20 damage,
you still have 30 health so be careful.
You pull out your magic wand and hold it at
your side.""")
  prompt = f"""Which spell would you like to use?
{spells}. \nSPELL: """

  while True:
    key = input(prompt)

    if key == 'flame thrower':
      print("""Used flame thrower!
You did 20 damage to your enemy!""")
      break
    if key == 'special attack':
      print("""Used special attack!
You did 30 damage to your enemy!""")
      break
    elif key == 'final blow':
      print("""Used final blow!
You did 30 damage to your oponent.""")
      break
    elif key == 'quit':
      break
    else:
      print("Huh?")

  print("""\nYou killed the elf!
Now go into the next room before
another one comes. \n*go \n*quit game""")
  prompt = 'ACTION: '

# Player successfully escapes and finds
# another room with an item
  while True:
    key = input(prompt)

    if key == 'go':
      print("""\nGoing into the next room.
You enter a room with a table in the middle
and a bottle with mysterious liquid in it.
The label on the bottle says "Magic healing
potion that heals 20 damage".
You take it.""")
      break
      inv.inventory_list.append("Healing Potion")
    elif key == 'quit game':
      qg.quit_game()
    else:
      print("Huh? You can't do that here.")

  # Player uses potion before entering
  # the room before the final battle
  print("""\nComplete one of the following
actions: \n*use potion \n*open inventory
*quit game""")

  prompt = 'ACTION: '

  while True:
    key = input(prompt)

    if key == 'use potion':
      print("""Drank potion. You are
now fully healed with 60 health. You go into the
dark room to fully prepare yourself for
the battle. With wand in hand you read the
sign above the final room that says 'KING BULBIN
ROOM'. You walk through the door.""")
      eog.ending()
      break
    elif key == 'open inventory':
      inv.open_inventory()
    elif key == 'quit game':
      qg.quit_game()
    else:
      print("Huh? You can't do that here.")
