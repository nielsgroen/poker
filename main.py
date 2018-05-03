import numpy as np
from cards import Cards
from player import Player
from game import Game
from card import Card

# initialize cards: Done
# instantiate Player(s): Done
# instantiate Game: Done
# TODO instantiate Round(s)
# give Player a Hand: Done
# TODO check for best Hand
# TODO distribute the moolah

# TODO create GUI

# TODO create UtilityFunction U(money)
players = [Player('Henk', 1100), Player('Bep', 200)]

game = Game(players)
print(game)