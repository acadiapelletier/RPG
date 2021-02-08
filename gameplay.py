# Course: CS 30
# Period: morning
# Date created: 21 / 02 / 08
# Name: Acadia Pelletier
# Description: RPG Continuous Game Play Assignment

# Lists out all available actions
print("""Go in one of the following directions: 
    *forward \n\t*left \n\t*right \n\t*back""")
print("""Complete one of the actions:
    *fight \n\t*run""")
print("Type 'quit' to stop.")

prompt = 'Action: '

# Completes available actions
while True:
  action = input(prompt)

  if action == 'forward':
    print("Going forward!")
  elif action == 'left':
    print("Going left!")
  elif action == 'right':
    print('Going right!')
  elif action == 'back':
    print('Going back!')
  elif action == 'fight':
    print('Fight!')
  elif action == 'run':
    print('Run!')
  elif action == 'quit':
    print("quit!")
    break
  else:
    print("""Huh? That's not an 
action you can take!""")
