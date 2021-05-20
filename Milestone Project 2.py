#!/usr/bin/env python
# coding: utf-8

# In[24]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True


# In[25]:


class Card:
    
    def __init__(self,suit,rank):
        
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        
        return self.rank + ' of ' + self.suit


# In[26]:


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp


    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        card_one=self.deck.pop()
        return card_one


# In[27]:


test_deck = Deck()
print(test_deck)


# In[28]:


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


# In[29]:


class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# In[30]:


def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("Enter your bet:"))
        except:
            print("Please enter a number")
        else:
            if chips.bet > chips.total:
                print("Sorry not enough chips")
            else:
                break
        
    


# In[31]:


def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# In[32]:


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        player_input=input("Do you want to hit or stand?")
        if player_input== "hit":
            hit(deck,hand)
        elif player_input== 'stand':
            print('Player stands, Dealer is playing.')
            playing=False
        else:
            print('Error!!, Please enter hit or stand.')  
            continue
            
        break


# In[33]:


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


# In[34]:


def player_busts(player,dealer,chips):
    print('Player lost!! BUST')
    chips.lose_bet()
    

def player_wins(player,dealer,chips):
    print('Player Wins!!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer BUSTS! Player wins')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('Dealer wins!! Better luck next time xD')
    chips.lose_bet()
    
def push(player,dealer):
    print("It's a tie! PUSH")


# In[37]:


while True:
    
    print("Welcome to Anas's Casino! \n     BLACKJACK   ")
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips = Chips()
    
    take_bet(player_chips)

    show_some(player_hand,dealer_hand)
    while playing:
        
        hit_or_stand(deck,player_hand)       
        show_some(player_hand,dealer_hand)       
        if player_hand.value > 21:
        player_busts(player_hand,dealer_hand,player_chips)  
        break
            
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        show_all(player_hand,dealer_hand)
         if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
        
        
     
    print("No of chips remaining: {}".format(player_chips.total))
    
    play_again = input("Do you want to play again? Enter Y or N:")
    if play_again[0].upper()=="Y":
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break


# In[ ]:




