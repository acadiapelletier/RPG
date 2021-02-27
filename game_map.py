# Shows the enemy info in the mysterious book

def show_enemies():
  print(" ")
  print("""To help I've written down
some key info for you on your journey.
Remember this information well. It may come in handy.
Here is the list of potential enemies
you will come accross:""")
  print(" ")

  class Enemy():
    def __init__(self, name, traits, fighting_info):
      self.name = name
      self.traits = traits
      self.fighting_info = fighting_info

    def describe_enemy(self):
      message = f"""
Enemy type and name: {self.name}
Traits: {self.traits}
Fighting info: {self.fighting_info}"""
      print(message)

  enemy_oaf = Enemy('Oaf. King Bulbin',
["""Craves power""", 'Smelly',
'Anger issues'], """Hits hard, moves slow.
He has 60 health.""")

  enemy_elf = Enemy("Elves. They don't have names",
["""Loyal to the king""", "Live to serve the king",
"""They don't talk"""], """Attacks do
less damage but they move quicker.
They have 20 health.""")

  enemy_elf.describe_enemy()
  print(" ")
  enemy_oaf.describe_enemy()
