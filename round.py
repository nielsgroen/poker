from cards import Cards
import numpy as np
from player import Player
from deck import Deck
from cards import Cards
from card import Card

class Round:

    def __init__(self, players):
        self.players = players
        self.deck = None
        self.blind_index = 1
        # self.cards_table = Cards.cards_table

        # TODO fix small and big blind

    def play_round(self):
        # Pre-flop
        self._deal_cards()
        self._assign_blinds()
        self._pre_flop_bets()
        # Flop
        # Turn
        # River

        # Distribute money

        # Clear hands
        map(lambda player: player.set_hand(None, None), self.players)
        return self.players

    def _deal_cards(self):
        dealt_cards = []

        dealt_cards, new_cards = self._get_undealt_cards(dealt_cards, 5)
        self.deck = Deck(new_cards)

        for player in self.players:
            dealt_cards, new_cards = self._get_undealt_cards(dealt_cards, 2)
            player.set_hand(new_cards)

    def _get_undealt_cards(self, dealt_cards, n):
        new_cards = []

        generate_new = True
        while generate_new:
            card = Card(Cards.int_to_colour[np.random.randint(1, 5)], Cards.int_to_value[np.random.randint(2, 15)])
            if card != next(iter(list(filter(lambda item: item == card, dealt_cards)) or []), None):
                new_cards.append(card)
                dealt_cards.append(card)
            if len(new_cards) == n:
                generate_new = False

        return dealt_cards, new_cards

    def _assign_blinds(self):
        self.players[self.blind_index % len(self.players)].has_big_blind = False
        self.players[(self.blind_index - 1)% len(self.players)].has_small_blind = False

        self.blind_index += 1

        self.players[self.blind_index % len(self.players)].has_big_blind = True
        self.players[(self.blind_index - 1) % len(self.players)].has_small_blind = True

    def _pre_flop_bets(self): # TODO relay action, fix 'something'
        for i in range(len(self.players)):
            something = self.players[i % len(self.players)].decide_action()