# File for the ending of the game
# Spells list is for the spells available
# To the player
import quit_game as qg
import inventory as inv
import losegame as lg
spells = ['flame thrower', 'special attack',
'final blow']


def ending():

  # Fight start sequence
  # if the player choses the flame thrower
  # spell at any point they will lose
  # and be taken to losegame file
  print("""\nYou enter the final room.
In front of you the oaf, King Bulbin.
He wields a sword and is almost twice your size.
He looks in front of you and says "You dare
try and exit? You must fight me first!"
He holds his sword in the air as if ready
to fight.""")

  # Fight sequence
  print("""\nComplete one of the following
actions: \n*use spell \n*open inventory
*quit game""")

  prompt = 'ACTION: '

  while True:
    key = input(prompt)

    if key == 'use spell':
      print(f"""\nWhich spell would you
like to use? \n{spells}""")
      break
    elif key == 'open inventory':
      inv.open_inventory()
    elif key == 'quit game':
      qg.quit_game()
    else:
      print("Huh? You can't do that here.")

  prompt = 'SPELL: '

  while True:
    key = input(prompt)

    if key == 'flame thrower':
      print("""Used flame thrower!
You did 20 damage to your oponent""")
      lg.lose_game()
      lg.lose_game2()
    elif key == 'special attack':
      print("""Used special attack!
You did 30 damage to your oponent""")
      break
    elif key == 'final blow':
      print("""Used final blow!
You did 30 damage to your opponent""")
      break
    else:
      print("Huh? You can't do that here")

  print("""\nThe oaf hit you! He did 30 damage""")

  print(f"""\nWhich spell would you like to use?
{spells}""")

  prompt = 'SPELL: '

  while True:
    key = input(prompt)
    if key == 'flame thrower':
      print("""Used flame thrower!
You did 20 damage to your oponent""")
      lg.lose_game2()
    elif key == 'special attack':
      print("""You used special attack!
You did 30 damage to your opponent.""")
      break
    elif key == 'final blow':
      print("""You used final blow!
You did 30 damage to your opponent.""")
      break

  #If the player successfully defeats
  # the final boss, this message will show
  print("""\nYou did it! You dealed
a final blow the oaf and you watch as
he falls to the ground. "You won't get
away with this!" he yells. You see the
door behind him and make a run for it.
Finally victory \nCONGRATS ON THE VICTORY
THANK YOU FOR PLAYING!!!!!!!!""")
  import sys
  sys.exit()
