import numpy as np
import pandas as pd

class Cards:

    colours = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    card_names = [str(i) for i in range(1, 11)] + ['j', 'q', 'k', 'a']
    # cards_table = pd.DataFrame([['unassigned']*4], columns=colours, index=card_names)
    card_full_names = {'2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten', 'j': 'Jack', 'q': 'Queen', 'k': 'King', 'a': 'Ace'}
    int_to_value = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'j',
                         12: 'q', 13: 'k', 14: 'a'}
    int_to_colour = {1: 'Hearts', 2: 'Diamonds', 3: 'Clubs', 4: 'Spades'}

    def __str__(self):
        return self.cards_table.__str__()
