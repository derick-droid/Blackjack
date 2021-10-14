
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

# creating a class for a player


class Player:

    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.live_score()
        self.money = money
        self.bet = 0

    def __str__(self):  # printing player
        new_hand = " "
        for card in self.hand:
            new_hand += str(card) + " "
            final_hand = new_hand + " score : " + str(self.score)

        return final_hand

    def live_score(self):  # function for calculating the score
        self.score = 0

        # dictionary of scores
        card_values = {
            "A": 11,
            "j": 10,
            "Q": 10,
            "K": 10,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10
        }
        a_counter = 0

        for card in self.hand:

            self.score += card_values[card]

            # keeping track of As
            if card == "A":
                a_counter += 1
            if self.score > 21 and a_counter != 0:
                self.score -= 10
                a_counter -= 1

        return self.score

    def hit_card(self, card):  # hitting another card
        self.hand.append(card)
        self.score = self.live_score()

    def play(self, another_hand):  # creating another hand

        self.hand = another_hand
        self.score = self.live_score()

    def pay(self, amount): # function for making payment
        self.money -= amount

    def win(self, result):  # a function to calculate the win
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money = (2.5 * self.bet)
            else:
                self.money += (2 * self.bet)
            self.bet = 0
        else:
            self.bet = 0

    def bet_money(self, amount):
        self.money -= amount
        self.bet += amount


first_player = Player(["A", "A", "2", "A"])
first_player.hit_card("A")
print(first_player)
first_player.play(["K", "10"])
print(first_player)
first_player.bet_money(30)
print(first_player.money, first_player.bet)
first_player.win(True)
print(first_player.money, first_player.bet)
print(first_player.money)
first_player.win(20)
print(first_player.money)
