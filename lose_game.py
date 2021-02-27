import end_of_game as eog
import quit_game as qg
spells = ['flame thrower', 'special attack',
'final blow']


def lose_game():
  print("""\nThe oaf hit you! He did 30 damage""")

  print(f"""\nWhich spell would you like to use?
{spells}""")

  prompt = 'SPELL: '

  while True:
    key = input(prompt)

    if key == 'flame thrower':
        print("""You used special attack!
You did 20 damage to your opponent.""")
    if key == 'special attack':
      print("""You used special attack!
You did 30 damage to your opponent.""")
      break
    elif key == 'final blow':
      print("""You used final blow!
You did 30 damage to your opponent.""")
      break


def lose_game2():
  print("""\nOh no! The oaf hit you once more.
The 30 damage he dealt was fatal. You fall
to the ground as you have no more energy to
deal another hit.
The oaf laughs at your failure.""")

  prompt = '\nWould you like to try again? '

  while True:
    key = input(prompt)

    if key == 'yes':
      eog.ending()
    elif key == 'no':
      qg.quit_game()
    else:
      print("Huh? You can't do that here.")
