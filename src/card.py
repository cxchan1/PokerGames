#!/usr/bin/python

# Parse the cards draw from the deck into readable object
class Card:
    numberLookup = {"0": 10, 10: 10, "10": 10, "T": 10, "JACK": 11, "J": 11, "QUEEN": 12, "Q": 12, "KING": 13, "K": 13, "ACE": 14, "A": 14 }

    def __init__(self, carddata):
        if isinstance(carddata, str):
            self.value = carddata[0]
        elif isinstance(carddata, dict):
            self.value = carddata['value']
        else:
            raise ValueError

        # Assign numeric value to card
        if self.value in self.numberLookup:
            if self.value == "JACK":
                self.value = "J"
            elif self.value == "QUEEN":
                self.value = "Q"
            elif self.value == "KING" or self.value == "K":
                self.value = "K"
            elif self.value == "ACE":
                self.value = "A"
            elif self.value == 10 or self.value == "10":
                self.value = "T"
            # elif self.value == "JOKER" or self.value == "*":
            #     self.value = "*"
            self.number = self.numberLookup[self.value]
        else:
            try:
                self.number = int(self.value)
            except ValueError:
                print('Invalid card: {}'.format(carddata))
                raise
