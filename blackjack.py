#!/usr/bin/env python
# coding: utf-8

# BlackJack Python Terminal game

# In[1]:


import random


# In[2]:


class Deck:
    def new_deck(self):
        deck = 4*[x for x in range(2, 11)]
        deck.sort()
        tens = ['J', 'Q', 'K']
        ace = 'A'
        deck += 4*tens
        deck += ['A' for a in range(4)]
        return deck
    
    def __init__(self):
        self.cards = self.new_deck()
    
    def select_random_card(self):
        return random.choice(self.cards)
    
    def deal_card(self, player):
        if len(self.cards) == 0:
            self.cards = self.new_deck()
        selection = self.select_random_card()
        player.cards.append(selection)
        self.cards.remove(selection)
        return selection


# In[3]:


class Player:
    def __init__(self, name, chips=0, banker=False, cards=None, value=0, bust=False, blackjack= False):
        self.chips = chips
        self.banker = banker
        self.cards = []
        self.value = value
        self.bust = bust
        self.blackjack = False
        self.name = name
        
    def check_blackjack(self):
        if self.value == 21:
            self.blackjack = True
            return True
    
    def check_bust(self):
        if self.value > 21:
            self.bust = True
            return True
        else:
            self.bust = False
            return False
    
    def check_value(self):
        value = 0
        tens = ['J', 'Q', 'K']
        for card in self.cards:
            if card not in tens and card != 'A':
                value += card
            elif card in tens:
                value += 10
            elif card == 'A':
                if value + 11 <= 21:
                    value += 11
                else:
                    value += 1
        self.value = value
        print(f"New card: {card}, total: {self.value}")
        if self.check_bust():
            
            print("You're bust!")
        return value


# In[13]:


class Game:
    def __init__(self):
        self.player1 = Player(chips=500, name = "Player 1")
        self.banker = Player(banker=True, name = "Dealer")
        self.card_deck = Deck()
        self.players = [self.player1, self.banker]
    
    def deal_first_cards(self):
        for i in range(2):
            self.card_deck.deal_card(self.player1)
            self.card_deck.deal_card(self.banker)
        self.player1.check_value()
        self.banker.check_value()
        if self.player1.check_blackjack():
            print("Player has Blackjack!")
        if self.banker.check_blackjack():
            print("Banker has Blackjack!")
        
        self.display_cards()
            
    def display_cards(self):
        print(f"Player 1 cards: {self.player1.cards}, value: {self.player1.value}")
        print(f"Banker cards: {self.banker.cards}, value: {self.banker.value}")
        
    def turn(self, player):
        # player's go
        stick = False
        while stick == False:
            option = input("Do you want to stick or twist?")
            if option == 'twist':
                self.card_deck.deal_card(player)
                player.check_value()
                if player.bust:
                    break
            if option == 'stick':
                stick = True
        # banker's go
        print("Dealer's go")
        if player.bust == False:
            while player.value > self.banker.value:
                self.card_deck.deal_card(self.banker)
                self.banker.check_value()
                if self.banker.value == 21:
                    print("Dealer sticks")
                    break
                if self.banker.bust:
                    print("Dealer's bust")
                    break
                elif self.banker.value >= player.value:
                    print("Dealer sticks")
                    break
    
    def who_wins(self):
        winning_score = 0
        for player in self.players:
            if player.bust == False and player.value > winning_score:
                winning_score = player.value
                winner = player
        return winner
    
    def round_winner(self):
        win = self.who_wins()
        print(f"{win.name} wins!")


# In[14]:


game = Game()


# In[15]:


game.deal_first_cards()


# In[16]:


game.turn(game.player1)


# In[17]:


game.display_cards()


# In[18]:


for player in game.players:
    print(player.value)


# In[19]:


game.round_winner()


# In[20]:


game.player1.bust


# In[21]:


game.banker.bust


# In[ ]:




