# Testing template for the Hand class


import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


#####################################################
# Student should insert code for Hand class here
class Hand:
    def __init__(self):
        # create Hand object
        self.card = []

    def __str__(self):
        # return a string representation of a hand
        ans = ""
        for i in range(len(self.card)):
            ans += self.card[i].suit
            ans += self.card[i].rank
            ans += " "
        return 'Hand contains ' + ans

    def add_card(self, card):
        # add a card object to a hand
        return self.card.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        global VALUES
        tot_value = 0
        for i in range(len(self.card)):
            tot_value += VALUES[self.card[i].rank]
        for i in range(len(self.card)):
            if (self.card[i].rank == 'A') and (tot_value + 9 <= 21):
                tot_value += 9
                return tot_value
            else:
                return tot_value
   
    def draw(self, canvas, pos):
        for i in range(len(self.card)):
            card_loc = (card_size[0] * (0.5 + RANKS.index(self.card[i].rank)), card_size[1] * (0.5 + SUITS.index(self.card[i].suit)))
            canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)

###################################################
# Test code

c1 = Card("S", "A")
c2 = Card("C", "2")
c3 = Card("D", "T")
print c1, c2, c3
print type(c1), type(c2), type(c3)

test_hand = Hand()
print test_hand

test_hand.add_card(c1)
print test_hand

test_hand.add_card(c2)
print test_hand

test_hand.add_card(c3)
print test_hand

print type(test_hand)


###################################################
# Output to console
# note that the string representation of a hand will 
# vary based on how you implemented the __str__ method

#SA C2 DT
#<class '__main__.Card'> <class '__main__.Card'> <class '__main__.Card'>
#Hand contains 
#Hand contains SA 
#Hand contains SA C2 
#Hand contains SA C2 DT 
#<class '__main__.Hand'>