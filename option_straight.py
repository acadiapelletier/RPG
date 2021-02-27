# File for if the player chose the go straight
# Spells list is for the spells available
# To the player
import inventory as inv
import quit_game as qg
import end_of_game as eog
spells = ['flame thrower', 'special attack',
'final blow']


def option_straight():
  #Player is in a room with a puzzle
  # the password sequence is the puzzle
  print("""\nYou find yourself in a new,
strange, room. What do you do?
*look around \n*open inventory
*quit game""")
  prompt = 'ACTION: '

  while True:
    key = input(prompt)

    if key == 'look around':
      print("""You look around the new room
and find the door to be locked. Beside it
there is a keypad.
Would you like to investigate?""")
      break
    elif key == 'open inventory':
      inv.open_inventory()
    elif key == 'quit game':
      qg.quit_game()
    else:
      print("Huh? You can't do that here.")

  prompt = 'ACTION: '

  while True:
    key = input(prompt)

    if key == 'yes':
      print("""\nYou walk towards the keypad.
It is a letter password instead. Beside
the keypad there is a note that reads:
"HINT: Password is who we live to serve."
I wonder who they are referring to. Try put in a
password.""")
      break
    elif key == 'no':
      print("""\nOK. Guess you're stuck here
forever.""")
      import sys
      sys.exit()
    else:
      print("Huh?")

  # The player inputs the password here
  prompt = 'PASSWORD: '

  while True:
    key = input(prompt)

    if key == 'king bulbin':
      print("A message shows saying: Password correct.")
      break
    elif key == 'King Bulbin':
      print("A message shows saying: Password correct.")
      break
    else:
      print("No that's not right. Try again.")

  print("""\nThe door opens!
Go through the door. \n*go \n*quit game""")

  prompt = 'ACTION: '

  #Final room before fighting the final boss
  while True:
    key = input(prompt)

    if key == 'go':
      print("Going into the next room.")
      break
    elif key == 'quit game':
      qg.quit_game()
    else:
      print("Huh? You can't do that here.")
  print("""\nYou enter a dark and dingy room.
There is nothing but darkness and a large door.
The door reads 'KING BULBIN ROOM'.
You are now ready for the final room.
Proceed with caution. \n*go into next room
*open inventory \n*quit game""")

  prompt = 'ACTION: '

  while True:
    key = input(prompt)

    if key == 'go into next room':
      eog.ending()
      break
    elif key == 'open inventory':
      inv.open_inventory()
    elif key == 'quit game':
      qg.quit_game()
    else:
      print("Huh? You can't do that here.")
