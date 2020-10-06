from hand import *
from result import *

# class HandTypes(enum.Enum):
#     Four_Of_A_Kind = 1
#     Full_House = 2
#     Straight = 3
#     Three_Of_A_Kind = 4
#     Two_Pair = 5
#     Pair = 6
#     High_Card = 7

# class Wild:
#     def __init__(self):
#         self.cards=[]
#         for card_data in cardlist:
#             if card_data == '*':
#                 self.handle_wild_card(cardlist)
#             self.cards.append(Card(card_data))
#         self.valueCounter = Counter(card.number for card in self.cards)
#
# def handle_wild_card(self, cardlist):
#     for r in '23456789TJQKA':
#         temp = []
#         for card_data in cardlist:
#             if card_data == '*':
#                 temp.append(Card(r))
#             else:
#                 temp.append(Card(card_data))
#         for card in temp:
#             print(card.value)
#             print()
#
#     return