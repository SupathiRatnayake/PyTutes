# Take item into Hotbar
# START

# hotbar = ["pickaxe", "bread", "emerald"]
# inventory = ["sword", "wood"]

# GET inventory_item
# GET hotbar_slot

# SET inventory_index
# SET hotbar_item = hotbar[hotbar_slot]

# SET hotbar[hotbar_slot] = inventory_item
# SET inventory[inventory_index] = hotbar_item

# PRINT hotbar
# PRINT inventory
# END

hotbar = ["pickaxe", "bread", "emerald", None, None, None, None, None, "torch"]
inventory = ["sword", "wood"]

print("Hotbar: ", hotbar)
print("Inventory: ", inventory)
print("\n")

inventory_item = input("Enter item to swap: ")
hotbar_slot = int(input("Enter item to swap(1-9): ")) -1

# Swapping
hotbar_item = hotbar.pop(hotbar_slot)
inventory_index = inventory.index(inventory_item)
inventory.remove(inventory_item)
hotbar.insert(hotbar_slot, inventory_item)
inventory.insert(inventory_index, hotbar_item)

print("\n")
print("Hotbar: ", hotbar)
print("Inventory: ", inventory)
