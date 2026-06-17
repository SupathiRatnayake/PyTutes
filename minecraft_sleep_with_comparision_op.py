# Minecraft Sleep Check

# START
# dimension = 0
# blocks_to_bed = 5
# time = 6
# blocks_to_monster = 8
#
# IF not overworld:
#   PRINT "Alex was killed by [Intentional Game Design]"

# ELSE IF blocks_to_bed is greater than 3:
#   PRINT "You may not rest now; the bed is too far away"

# ELSE IF time less than 6:
#   PRINT "You can sleep only at night or during thunderstorms"

# ELSE IF blocks_to_monster less than or equal to 8:
#   PRINT "You may not rest now; there are monsters nearby"

# ELSE
#   PRINT "Sweet dreams! Skipping to morning..."

# STOP

dimension = 0
blocks_to_bed = 3
time = 6
blocks_to_monster = 9

if dimension != 0:
    print("Alex was killed by [Intentional Game Design]")
elif blocks_to_bed > 3:
    print("You may not rest now; the bed is too far away")
elif time < 6:
    print("You can sleep only at night or during thunderstorms")
elif blocks_to_monster <= 8:
    print("You may not rest now; there are monsters nearby")
else:
    print("Sweet dreams! Skipping to morning...")
