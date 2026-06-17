# Taking only 1 item from chest
# START
# inventory = []
# loot_chest = ["pickaxe", "bread", "emerald"]
# GET picked_item
# SET inventory[0] = picked_item
# PRINT inventory
# PRINT loot_chest
# END

inventory = []
loot_chest = ["pickaxe", "bread", "emerald"]

print("1.", loot_chest[0], "2.", loot_chest[1],"3.", loot_chest[2])
picked_index = int(input("Select Item: ")) -1

inventory.append(loot_chest.pop(picked_index))

print(inventory)
print(loot_chest)
