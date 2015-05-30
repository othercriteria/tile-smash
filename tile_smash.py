#!/usr/bin/env python

import numpy as np

# Simulation parameters
deck_reps = 10
game_reps = 10

# Game parameters
favor_more = True
cards_drawn = 3

# Deck design
#
# Cards:
#   d: dead end
#   l: left
#   s: straight
#   r: right
#   ls, lr, sr, lsr: combinations
deck_contents = { 'd': 10,
                  'l': 5, 's': 5, 'r': 5,
                  'ls': 5, 'lr': 5, 'sr': 5,
                  'lsr': 15 }

for deck_rep in range(deck_reps):
    deck = []
    for card in deck_contents:
        count = deck_contents[card]
        deck.extend([card] * count)
        
    for game_rep in range(game_reps):
        print(deck_rep, game_rep)
        np.random.shuffle(deck)

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
