# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
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
            if (self.card[i].rank == 'A') and (tot_value + 10 <= 21):
                tot_value += 10
        return tot_value
   
    def draw(self, canvas, pos):
        for i in range(len(self.card)):
            card_loc = (card_size[0] * (0.5 + RANKS.index(self.card[i].rank)), card_size[1] * (0.5 + SUITS.index(self.card[i].suit)))
            canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.card = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.card.append(Card(SUITS[i],RANKS[j]))

    def shuffle(self):
        # add cards back to deck and shuffle
        return random.shuffle(self.card)

    def deal_card(self):
        # deal a card object from the deck
        return self.card.pop()
    
    def __str__(self):
        # return a string representing the deck
        ans = ""
        for i in range(len(self.card)):
            ans += self.card[i].suit
            ans += self.card[i].rank
            ans += " "
        return ans
    
#define event handlers for buttons
def deal():
    global outcome, in_play
    # your code goes here
    global dealer, player, stack
    
    # MY GLOBAL VARIABLES
    dealer = Hand()
    player = Hand()
    stack = Deck()
    
    stack.shuffle()
    
    d1 = stack.deal_card()
    d2 = stack.deal_card()
    dealer.add_card(d1)
    dealer.add_card(d2)
    
    p1 = stack.deal_card()
    p2 = stack.deal_card()
    player.add_card(p1)
    player.add_card(p2)
    
    print dealer.get_value(), player.get_value()
    print dealer, player
    
    in_play = True

def hit():
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric