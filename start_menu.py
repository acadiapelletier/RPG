# Main menu, start screen

print("""Welcome to [REDACTED]
Choose one of the following options: \n*start game \n*quit""")

prompt = 'ACTION: '

while True:
  key = input(prompt)

  if key == 'start game':
    print("Starting game...")
    import game as game
  elif key == 'quit':
    print("Quitting game...")
    import sys
    sys.exit()
  else:
    print("Try again")
