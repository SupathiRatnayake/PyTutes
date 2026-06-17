# Minecraft Drowned attack check w/ Logical

# START

# isNight = True
# weather = "rain"
# distance_to_player = 8

# IF (night or weather is not clear) and player distance <= 16:
#   PRINT "The Drowned comes to attack"

# ELSE
#   PRINT "The Drowned stays passive"

# STOP

is_night = False
weather = "rain"
distance_to_player = 18

if (is_night or weather is not "clear") and distance_to_player <= 16:
    print("The Drowned comes to attack")
else:
    print("The Drowned stays passive")

