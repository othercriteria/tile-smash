#!/usr/bin/env python

import numpy as np

# Using mod-4 arithmetic for cardinal directions
# 0: ( 1,  0)
# 1: ( 0,  1)
# 2: (-1,  0)
# 3: ( 0, -1)
def rotate_by(card, r):
    n = [((c + r) % 4) for c in card]
    n.sort()
    return tuple(n)
def translate_by(loc, d):
    x, y = loc
    if d == 0:
        return (x+1, y)
    elif d == 1:
        return (x, y+1)
    elif d == 2:
        return (x-1, y)
    else:
        return (x, y-1)

# Simulation parameters
deck_reps = 10
game_reps = 10

# Game parameters
favor_more = True
cards_drawn = 3
initial = { (0,0): (0,1,3) }
exit = (-1,0)

# Deck design
#
# Cards:
#   0: straight
#   1: left
#   3: right
deck_contents = { tuple(): 10,
                  (0,): 5, (1,): 5, (3,): 5,
                  (0,1): 5, (0,3): 5, (1,3): 5,
                  (0,1,3): 15 }

for deck_rep in range(deck_reps):
    deck = []
    for card in deck_contents:
        count = deck_contents[card]
        deck.extend([card] * count)
        
    for game_rep in range(game_reps):
        print(deck_rep, game_rep)
        np.random.shuffle(deck)

        # Initialize board
        placed = set()
        open = []
        for loc in initial:
            placed.add(loc)
            for dir in initial[loc]:
                open.append((loc, dir))

        deck_mut = deck.copy()
        while len(deck_mut) > 0:
            draws = []
            for d in range(cards_drawn):
                if len(deck_mut) > 0:
                    draws.append(deck_mut.pop())

            if favor_more:
                most = max([len(c) for c in draws])
                draws = [d for d in draws if len(d) == most]

            # Redundant when added, but check before removing
            np.random.shuffle(draws)
            draw = draws[0]

            while len(open) > 0:
                np.random.shuffle(open)
                open_loc, open_dir = open.pop()
                place_loc = translate_by(open_loc, open_dir)

                # Can't place in a location with an existing tile
                if place_loc in placed: continue

                placed.add(place_loc)
                for dir in rotate_by(draw, open_dir):
                    open.append((place_loc, dir))
                break

        print(exit in placed)
