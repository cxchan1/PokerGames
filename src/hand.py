#!/usr/bin/python

import enum
from card import *
from collections import Counter

class HandTypes(enum.Enum):
    Four_Of_A_Kind = 1
    Full_House = 2
    Straight = 3
    Three_Of_A_Kind = 4
    Two_Pair = 5
    Pair = 6
    High_Card = 7

class Hand:
    def __init__(self, cardlist):
        self.cards=[]
        for card_data in cardlist:
            if card_data == '*':
                new_hand = self.handle_wild_card(cardlist)
                self.cards = new_hand if len(new_hand) != 0 else []
                break
            else:
                self.cards.append(Card(card_data))
        self.valueCounter = Counter(card.number for card in self.cards)

    def toConsole(self):

        string = ''.join((c.value) for c in self.cards)
        return string

    # classify hand. only designed for 5 card hands.
    def classify(self):
        if len(self.cards) != 5:
            return None
        maxValueCount = max(self.valueCounter.values())
        isStraight = (maxValueCount == 1) & (max(self.valueCounter.keys())-min(self.valueCounter.keys()) == 4)
        topCard = max(self.valueCounter.keys())

        # classification order is highest -> lowest, return when match is found
        if maxValueCount == 4:
            return HandTypes.Four_Of_A_Kind
        elif (maxValueCount == 3 and len(self.valueCounter) == 2):
            return HandTypes.Full_House
        elif isStraight:
            return HandTypes.Straight
        elif maxValueCount == 3:
            return HandTypes.Three_Of_A_Kind
        elif maxValueCount == 2:
            if len(self.valueCounter) == 3:
                return HandTypes.Two_Pair
            else:
                return HandTypes.Pair
        else:
            return HandTypes.High_Card

    def getvalue(self):
        classify = self.classify()
        if classify == HandTypes(7):
            return 1
        elif classify == HandTypes(6):
            return 2
        elif classify == HandTypes(5):
            return 3
        elif classify == HandTypes(4):
            return 4
        elif classify == HandTypes(3):
            return 5
        elif classify == HandTypes(2):
            return 6
        elif classify == HandTypes(1):
            return 7

    def getlist(self):
        list = []
        for c in self.cards:
            list.append(c.number)
        list.sort()
        return list

    # return a new hand with the best value from the wild card
    def handle_wild_card(self, cardlist):
        result = []
        highest_rank = 1
        for r in "23456789TJQKA":
            self.cards=[]
            for card_data in cardlist:
                if card_data == '*':
                    self.cards.append(Card(r))
                else:
                    self.cards.append(Card(card_data))
            self.valueCounter = Counter(card.number for card in self.cards)
            if highest_rank < self.getvalue():
                highest_rank = self.getvalue()
                result = self.cards
        return result
