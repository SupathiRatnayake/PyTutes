# Minecraft Sleep Check
# START
# IF monsters nearby
#   Cannot Sleep when monsters nearby
# ELSE IF it is not night
#   You can only sleep at night
# ELSE
#   Sleep

is_monsters_nearby = True
is_daytime = True
is_bed_far = True

if is_bed_far:
    print("You may not rest now; the bed is too far away")
elif is_daytime:
    print("You can only sleep at night!")
elif is_monsters_nearby:
    print("You may not rest now, there are monsters nearby!")
else:
    print("Sweet dreams! Skipping to morning...")

print("ending if")
