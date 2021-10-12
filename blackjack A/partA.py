
from random import shuffle


def cards():

    real_cards = []
    list_cards = ["A", "Q", "J", "K", ]
    for play in range(4):  # for different suits
        for card in list_cards:
            real_cards.append(card)
        for numbers in range(2, 11):
            real_cards.append(str(numbers))

    shuffle(real_cards)
    print(real_cards)
    return real_cards


card_deck = cards()



# # creating class for the players
#
# class Player:
#
#     def __init__(self, hand=[], money=100,):
#         self.money = money
#         self.hand = hand
#         self.score = self.score()
#
#     def __str__(self):
#
#         new_hand = ""
#         for card in self.hand:
#             new_hand += str(card) + " "
#         final_status = new_hand + " score: " + str(self.score)
#
#         return final_status
#
#     def score(self):
#
#         self.score = 0
#
#         # scores for each card
#         letter_card = {
#             "A": 11,
#             "J": 10,
#             "Q": 10,
#             "K": 10,
#             "2": 2,
#             "3": 3,
#             "4": 4,
#             "5": 5,
#             "6": 6,
#             "7": 7,
#             "8": 8,
#             "9": 9,
#             "10": 10
#         }
#
# # checking for As so that we cannot re use the As for our benefit
#
#         A_counter = 0
#
#         for one_card in self.hand:
#             self.score += letter_card[one_card]
#             if one_card == "A":
#                 A_counter += 1
#             if self.score > 21 and A_counter != 0:
#                 self.score -= 10
#                 A_counter -= 1
#         return self.score
#
#
# def hit_card(self, card):
#     self.hand.append(card)
#     self.score = self.score()
#
#
# playerA = Player(["3", "7", "A", "A", "A"])
# print(playerA)
# playerA.hit_card("k")
#
# cards()
