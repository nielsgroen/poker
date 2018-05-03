

class Card(object):

    def __init__(self, colour, value):
        self.colour = colour
        self.value = value

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.colour == other.colour and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '{0}: {1}'.format(self.colour, self.value)