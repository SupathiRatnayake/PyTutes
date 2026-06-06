# Minecraft Sleep Check
# START
# IF bed is near
#       IF it is night
#           IF no monsters nearby
#               Sleep
#           ELSE
#              Cannot Sleep when monsters nearby
#       ELSE
#           You can only sleep at night
# ELSE
#   the bed is too far away

no_monsters_nearby = False
is_nighttime = True
is_bed_close = True

if is_bed_close:
    if is_nighttime:
        if no_monsters_nearby:
            print("Sweet dreams! Skipping to morning...")
        else:
            print("You may not rest now, there are monsters nearby!")
    else:
        print("You can only sleep at night!")
else:
    print("You may not rest now; the bed is too far away")

print("Rest of the program")
