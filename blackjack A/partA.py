
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
