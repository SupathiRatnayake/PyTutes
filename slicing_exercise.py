most_played_games = [
    "Tetris",                   # Index 0: ~520+ million copies (All versions combined)
    "Minecraft",                # Index 1: ~350+ million copies
    "Grand Theft Auto V",       # Index 2: ~225+ million copies
    # Missing some
    "PUBG: Battlegrounds",      # Index 6: ~75 million copies
    "Super Mario Bros.",        # Index 7: ~65 million copies
    "Terraria",                 # Index 8: ~64 million copies
    "The Witcher 3: Wild Hunt"  # Index 9: ~60 million copies
]

missing_items = [
    "Wii Sports",               # Index 3: ~82.9 million copies
    "Red Dead Redemption 2",    # Index 4: ~82 million copies
    "Mario Kart 8 / Deluxe",    # Index 5: ~79 million
]

# Insert missing items
# Get top 3 most selling games
# Get bottom 3 most selling games

most_played_games[3:3] = missing_items
# print("Complete list: ", most_played_games)
print("Top 3 most selling: ", most_played_games[:3])

print("Bottom 3 most selling: ", most_played_games[-3:])

