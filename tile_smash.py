#!/usr/bin/env python

import numpy as np

# Using mod-4 arithmetic for cardinal directions
def rotate_by(card, r):
    n = [((c + r) % 4) for c in card]
    n.sort()
    return tuple(n)

# Simulation parameters
deck_reps = 10
game_reps = 10

# Game parameters
favor_more = True
cards_drawn = 3

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
        #
        # Directions
        placed = { (0,0): (0,) }

        deck_mut = deck.copy()
        while len(deck_mut) > 0:
            draws = []
            for d in range(cards_drawn):
                if len(deck_mut) > 0:
                    draws.append(deck_mut.pop())

            if favor_more:
                most = max([len(c) for c in draws])
                draws = [d for d in draws if len(d) == most]

            print(draws)
            print([rotate_by(c,1) for c in draws])
