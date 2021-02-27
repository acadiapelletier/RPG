# Quits the game if the player inputs
# 'quit game' option during the game

def quit_game():
  prompt = """Are you sure you want to quit?
(type yes or no) """

  while True:
    key = input(prompt)

    if key == 'yes':
      print("Quitting game...")
      import sys
      sys.exit()
    elif key == 'no':
      print("Continue gameplay...")
      break
    else:
      "Huh?"
