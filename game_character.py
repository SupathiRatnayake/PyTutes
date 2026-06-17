# START
# GET name
# GET character type (wizard, fighter, healer)
# GET weapon = 
#   (wizard: staff/wand,
#    fighter: sword/axe,
#    healer: healing potion/ ressurection stone)
# SET health 100
# SET magic_abilities = fighter? no: yes
# SET attack_multiplier = fighter? 1.75: 1
# SET player = [name, type, weapon, health, magic_abilities, attack_multiplier]
# PRINT player

name = input("Enter player name: ")
characters = ["wizard", "fighter", "healer"]
print("1.", characters[0], "2.", characters[1], "3.", characters[2])
character = int(input("Enter Character: ")) - 1
weapons = [["staff", "wand"],
           ["sword", "axe"],
           ["healing potion", "ressurection stone"]]
print("1.", weapons[character][0],"2.", weapons[character][1])
weapon = int(input("Enter Weapon: ")) - 1
health = 100
magic_abilities = character != 1
attack_multiplier = 1.75 if character == 1 else 1

player = [name,
          characters[character],
          weapons[character][weapon],
          health,
          magic_abilities,
          attack_multiplier]

print(player)




