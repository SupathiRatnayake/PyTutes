# Breaking loot chest
# START
# inventory = ["axe"]
# loot_chest = ["pickaxe", "bread", "emerald"]
# PROMPT "Hit enter to break chest"
# PRINT "You broke the chest. Items splashed everywhere,
#           but finally you collected them all."
# APPEND all items in loot_chest into inventory
# DELETE loot_chest
# PRINT inventory 
# PRINT loot_chest
# END

inventory = ["axe"]
loot_chest = ["pickaxe", "bread", "emerald"]

input("Hit enter to break chest")
print('''You broke the chest. Items splashed everywhere,
      but finally you collected them all.''')

inventory.extend(loot_chest)
del loot_chest

print(inventory)
print(loot_chest)
