# Import necessary files
import inventory as inv
import quit_game as qg
import optionleft as ol
import optionstraight as os

# Start of the game
print(" ")
print("""Hello human... It appears
you have been trapped in a dungeon.
If you look to your left you can
see there is some sort of book
and map. Try picking it up by typing 'pick up'.""")

prompt = 'ACTION: '

while True:
  key = input(prompt)

  if key == 'pick up':
    print("""You have picked up a new item!
You can view it in in your inventory.""")
    inv.inventory_list.append('mysterious book')
    break
  else:
    print("Huh? That is not an available action.")
print(" ")

# Teaches player how to use inventory
print("""Complete one of the following actions:
*open inventory \n*quit game""")

prompt = 'ACTION: '

while True:
  key = input(prompt)

  if key == 'open inventory':
    inv.open_inventory()
    break
  elif key == 'quit game':
    qg.quit_game()
  else:
    print("Huh? That is not an available action.")

# First room, the player needs to
# escape the dungeon
print("""\nYou are currently in the dungeon room.
In order to escape you need to find a key.
Try looking around for a key.""")
print("""Complete one of the following actions:
*look around \n*quit game""")

prompt = 'ACTION: '

while True:
  key = input(prompt)

  if key == 'look around':
    print("""\nYou look around the room.
Just outside of the dungeon there appears to
be a safe with a keypad. Try reaching for it.""")
    break
  elif key == 'quit game':
    qg.quit_game()
  else:
    print("Huh? You can't do that right now.")

print("""\nComplete one of the following actions:
*go to safe \n*quit game""")

prompt = 'ACTION: '

while True:
  key = input(prompt)

  if key == 'go to safe':
    print("""\nGoing towards the safe...""")
    break
  elif key == 'quit game':
    qg.quit_game()
  else:
    print("Huh? You can't do that right now.")

print("""Once you reach the safe you notice
a hint near the keypad. There is a sticky
note that reads:
"PASSWORD HINT: 1000 + 200 + 40 + 2".
Try entering the password.""")

prompt = 'PASSWORD: '

while True:
  key = input(prompt)

  if key == '1242':
    print("Successfully opened safe!")
    break
  else:
    print("That's not right. Try again.")

print("""\nYou look in the safe and see the
key. You pick up the key! Now try opening the
dungeon door. \n*use key""")

prompt = 'ACTION: '

while True:
  key = input(prompt)

  if key == 'use key':
    print("""Using key... door opened!""")
    break
  else:
    print("Huh? You can't do that here.")

# Player escapes the dungeon and is
# now in another room
print("""\nYou successfully exit the dungeon.
Outside of the dungeon you find yourself
in another room.""")
print("""Complete one of the following actions:
*look around \n*open inventory \n*quit game""")

prompt = 'ACTION: '

while True:
  key = input(prompt)

  if key == 'look around':
    print("""\nYou look around the room and
find a drawer. Try opening it. \n*open drawer""")
    break
  elif key == 'open inventory':
    inv.open_inventory()
  elif key == 'quit game':
    qg.quit_game()
  else:
    print("Huh? You can't do that here.")

prompt = 'ACTION: '

# Player recieves weapon for the game
while True:
  key = input(prompt)

  if key == 'open drawer':
    print("""\nYou open the drawer. Inside
you find a magic spellbook and wand.
You take them both and add them to
your inventory.""")
    inv.inventory_list.append('magic spellbook')
    inv.inventory_list.append('magic wand')
    break
  else:
    print("Huh? You can't do that here.")

print("""\nChoose one of the following actions:
*open inventory \n*quit game""")

prompt = 'ACTION: '

while True:
  key = input(prompt)

  if key == 'open inventory':
    inv.open_inventory()
    break
  elif key == 'quit game':
    qg.quit_game()
  else:
    print("Huh? You can't do that here.")

print("""\nExcellent! now that you have
something to defend yourself with let's
go out the door. \nComplete one of the following
actions:
*leave room \n*explore more \n*quit game""")

prompt = 'ACTION: '

while True:
  key = input(prompt)

  if key == 'leave room':
    print("""You have left the room
and entered a new one.""")
    break
  elif key == 'quit game':
    qg.quit_game
  elif key == 'explore more':
    print("""You look around the room
some more and find nothing new.""")
  else:
    print("Huh? You can't do that right now.")

# Player leaves the second room and finds
# themselves at a cross road, each option
# brings a different puzzle
print("""\nOnce leaving the room you enter
a new one that has a door on either side.
What do you do? \n*open inventory
*go left \n*go straight \n*quit game""")

prompt = 'ACTION: '

while True:
  key = input(prompt)

  if key == 'open inventory':
    inv.open_inventory()
  elif key == 'go left':
    print("Going through the left door.")
    ol.option_left()
    ol.option_left2()
    break
  elif key == 'go straight':
    print("Going through the door up ahead.")
    os.option_straight()
    break
  elif key == 'quit game':
    qg.quit_game()
    break
  else:
    print("Huh? You can't do that here.")
