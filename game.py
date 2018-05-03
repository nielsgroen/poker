import pandas as pd
from player import Player
from round import Round

class Game:

    def __init__(self, players):
        self.players = players
        self.game_over = False

        self.start_game()

    def __str__(self):
        return str([player.__str__() for player in self.players])

    def start_game(self):
        while not self.game_over:
            self._start_new_round()
            self.game_over = True

    def _start_new_round(self):
        round = Round(self.players)
        self.players = round.play_round()