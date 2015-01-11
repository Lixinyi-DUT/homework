# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images=simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png?")

CARD_BACK_SIZE = (73, 98)
CARD_BACK_CENTER = (200, 100)
card_back = simplegui.load_image("http://static.adzerk.net/Advertisers/a2d2a0e7e84b4506bc056cd1db3d9b98.png")  
#I' m really sorry that I can't load the picture the template gives, so I change a picture to implement the project.


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
        self.cards=[]
        pass	# create Hand object

    def __str__(self):
        result ="Hand contains"
        for c in self.cards:
          result += ' '+str(c)
        return  result
# return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)
    # add a card object to a hand

    def get_value(self):
        result=0
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        for c in self.cards:
            result += VALUES[c.get_rank()]
        
        for c in self.cards:
            if c.get_rank()=='A':
                if result + 10 <= 21:
                    result += 10
        return result
   
    def draw(self, canvas, pos):
        count=0;
        for c in self.cards:
            c.draw(canvas,[pos[0]+75*count,pos[1]])
            count += 1
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards=[]
        for s in SUITS:
            for r in RANKS:
                self.cards.append(Card(s,r))

    def shuffle(self):
        random.shuffle(self.cards)
        # shuffle the deck 

    def deal_card(self):
        c=self.cards.pop(-1)
        return c
    
    def __str__(self):
        result ="Deck contains"
        for c in self.cards:
          result += ' '+str(c)
        return  result

#define event handlers for buttons
def deal():
    global outcome, in_play
    global D, player, dealer
    D=Deck()
    player=Hand()
    dealer=Hand()
    D.shuffle()
    player.add_card(D.deal_card())
    player.add_card(D.deal_card())
    dealer.add_card(D.deal_card())
    dealer.add_card(D.deal_card())
    outcome="Hit or stand?"
    # your code goes here
    
    in_play = True

def hit():
    global D,player,outcome,in_play
    if in_play==True:
     if player.get_value()<=21:
        player.add_card(D.deal_card())
  
     if player.get_value()>21:
       outcome = "You have busted! New deal?"
       in_play=False
    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global player,dealer,D,outcome,in_play
    
    if player.get_value()>21:
       outcome = "You have busted! New deal?"
    else:
        while dealer.get_value() < 17:
            if dealer.get_value() < 21:
                dealer.add_card(D.deal_card())
                
        if dealer.get_value()> 21:
            outcome = "The dealer has busted! New deal?"
        else:
            if player.get_value() <= dealer.get_value():
                outcome = "The dealer wins by "+str(dealer.get_value()-player.get_value())+"! New deal?"
            else:
                outcome = "You win by "+str(-dealer.get_value()+player.get_value())+"! New deal?"
    
    in_play=False
                
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
   # card = Card("S", "A")
   # card.draw(canvas, [300, 300])
    global in_play,dealer,player,outcome
    canvas.draw_text("Blackjack",[270,100],35,'red')
    canvas.draw_text(outcome,[25,150],35,'white')
    canvas.draw_text("The dealer",[2,230],20,'white')
    canvas.draw_text("The player",[2,430],20,'white')
    dealer.draw(canvas,[100,200])
    player.draw(canvas,[100,400])
    if(in_play==True):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + 36.5, 200 + 49],CARD_BACK_SIZE )
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
