class Player:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bet = 0
        self.all_in = False
        self.has_small_blind = False
        self.has_big_blind = False

    def __str__(self):
        return 'Player {0}: ${1} {2}, {3}'.format(self.name, self.balance, self.hand[0], self.hand[1])

    def set_hand(self, card1, card2):
        self.hand = [card1, card2]

    def set_hand(self, cards):
        if len(cards) > 2:
            raise ValueError('Player {0} got dealt more than two cards'.format(self.name))
        self.hand = cards

    def get_hand(self):
        return self.hand

    def make_bet(self, amount): # TODO check if player goes all-in
        amount = max(amount, 0)
        if amount >= self.balance:
            self.all_in()
        else:
            self.balance -= amount
            self.bet += amount

    def fold(self):  # TODO make fold action
        pass

    def win_round(self, amount):
        self.balance += amount
        self.bet = 0
        self.all_in = False

    def lose_round(self): # TODO check if player is broke
        self.bet = 0

    def decide_action(self):
        user_input = input("Choose action for {0}: ${1}, check, bet, all-in, fold, call, raise: ".format(self.name, self.balance))
        user_input = user_input.split(' ')
