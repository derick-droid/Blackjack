
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
            "J": 10,
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

    # in case there is a win
    def win(self, result):  # a function to calculate the win
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money = (2.5 * self.bet)
            else:
                self.money += (2 * self.bet)
            self.bet = 0
        else:
            self.bet = 0

    # showing the betting money
    def bet_money(self, amount):
        self.money -= amount
        self.bet += amount

    # checking for black in the game
    def check_black(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False

    # if the game ends draw
    def draw_game(self):
        self.money += self.bet
        self.bet = 0


# hiding the computers score
def print_computer_player(computer_player):
    for card in range(len(computer_player.hand)):
        if card == 0:
            print("x", end=" ")
        elif card == len(computer_player.hand) - 1:
            print(card)
        else:
            print(computer_player.hand[card])


# initiating the playing of the game
card_play = cards()
first_hand = [card_play.pop(), card_play.pop()]
second_hand = [card_play.pop(), card_play.pop()]
first_player = Player(first_hand)
computer_player = Player(second_hand)

# determining the winner and blackjack
if first_player.check_black():
    if computer_player.check_black():
        first_player.draw_game()
    else:
        first_player.win(True)

# playing the game
while first_player.score < 21:

    user_action = input("Do you want another card: (y/n): ").lower()
    if user_action == "y":
        first_player.hit_card(card_play.pop())
        print(first_player)
        print_computer_player(computer_player)
    elif user_action == "n":
        print(first_player)
        print(computer_player)
    else:
        print("invalid option ")
        break
while computer_player.score < 16:
    computer_player.hit_card(card_play.pop())
