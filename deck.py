

class Deck(object):

    def __init__(self, cards_list):
        self.flop = cards_list[0:3]
        self.turn = cards_list[3:4]
        self.river = cards_list [4:5]
        self.deck = cards_list

    def __str__(self):
        return self.deck.__str__()
