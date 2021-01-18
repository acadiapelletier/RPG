## [Prerelease Version]

items = ['Key' , 'Magic Wand' , 'Secret Spellbook']
spells = ['Flame Thrower', 'Special Attack', 'Final Blow']

## Prints off available items in the inventory
print('Available items:')
for i, item in enumerate(items, 1):
  print(f"{i}. {item}")

## Prints off available spells in the inventory
print('Available spells')
for i, spell in enumerate(spells, 1):
  print(f"{i}. {spell}")
