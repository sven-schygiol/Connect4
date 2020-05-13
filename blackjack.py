import random
#create tuples for ranks and suits and a dictionary of values
suits = ('Hearts' , 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:
    """ Class of cards used to play the game, attributes are suit and rank.    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' +self.suit

    
class Deck:
    """Deck class, no attributes, can be shuffled and used to deal a single card."""
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_string = ''
        for card in self.deck:
            deck_string += card.__str__() + '\n'
        return 'The deck consists of:\n' + deck_string

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        """Deals a single card."""
        return self.deck.pop()
    
    
class Hand:
    """Hand class used for the player and dealer. Cards can be added to Hand.  """
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

            
class Chips:
    """ Chips class used to keep track of player's money. """
    def __init__(self):
        self.total = 0  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    bet = ''
    while type(bet) != int:
        try:
            bet = int(input('\nHow many chips would you like to bet? '))
        except ValueError:
            print('You must bet an integer value!')
        else:
            if bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
                bet = ''
    chips.bet = bet

def hit(deck,hand):
    """Adds a card to the hand in the Hand class, using a Deck. """
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    """Function prompting the player to receive another card or not."""
    #This controls the loop that determines whether it is the player's go or not. 
    global playing  
    #This loop ensures the correct input
    while True: 
        h_or_s = input(" Do you want to hit or stand? Type 'h' for hit or 's' for stand.   ")
        if h_or_s[0].lower() == 'h':
            break
        elif h_or_s[0].lower() == 's':
            break
        else:
            print("Please type an 'h' or an 's'.")
            continue
    if h_or_s[0].lower() == 'h':
        hit(deck,hand)
    elif h_or_s[0].lower() == 's':
        print("Player stands, dealer's turn.")
        playing = False
        
def show_some(player,dealer):
    """Reveals 1 of the dealer's cards and all of the players. """
    print("\n\nDealer's cards...")
    print("     First card hidden\n     " + str(dealer.cards[1]))
    print("\nPlayer's cards...")
    for card in player.cards:
        print('     ' + card.__str__())

def show_all(player,dealer):
    """Reveals all the dealer's cards as well as the players."""
    print("\n\nDealer's cards...")
    for card in dealer.cards:
        print('     ' + card.__str__())
    print("\nPlayer's cards...")
    for card in player.cards:
        print('     ' + card.__str__())

def player_busts(player):
    """Determines whether the player's Hand is over 21."""
    busts = False
    if player.value > 21:
        busts = True
    return(busts)

def player_wins(player,dealer):
    """Compares the player's and dealer's Hands determines if the player won."""
    if player.value > dealer.value:
        return(True)
    else:
        return(False)

def dealer_busts(dealer):
    """Determines whether the dealer's Hand is over 21."""
    if dealer.value > 21:
        return(True)
    else:
        return(False)
    
def dealer_wins(player, dealer):
    """Compares the player's and dealer's Hands determines if the dealer won."""
    if dealer.value > player.value and dealer.value <= 21:
        return(True)
    else:
        return(False)
    
def push(player, dealer):
    """Compares the player's and dealer's Hands determines if the game is a draw."""    
    if dealer.value == player.value:
        return(True)
    else:
        return (False)        


pchips = Chips()
pchips.total = 100
playing = True
while True: 
    print("\n\n\n\nHello and welcome to Blackjack!")
    
    #Creates a deck, deals two cards to the player and dealer
    game_deck = Deck()
    game_deck.shuffle()

    player = Hand()
    player.add_card(game_deck.deal())
    player.add_card(game_deck.deal())
    
    dealer = Hand()
    dealer.add_card(game_deck.deal())
    dealer.add_card(game_deck.deal())
    
    #Displays the number of chips, prompts for a bet. 
    print("Number of chips: " + str(pchips.total))
    if pchips.total == 0:
        print("You have no money left, resetting you back to 100")
        pchips.total  = 100
    take_bet(pchips)
    
    #Shows some cards before beginning playing loop.
    show_some(player, dealer)
    while playing:  
        

        hit_or_stand(game_deck,player)
        show_some(player,dealer)
        
        # If player's hand exceeds 21, breaks out of loop, and the player loses. 
        if player_busts(player) == True:
            print("\nPlayer has gone bust! You lose!")
            pchips.lose_bet()
            playing = False
            
        #The loop is exited when either the player goes bust or decides to stand.
        
# If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value < 22:
        
        while dealer.value <17:
            hit(game_deck, dealer)
        
        show_all(player,dealer)
        
        # Run different winning scenarios
        if player_wins(player, dealer):
            print("\nYou have won the game!")
            pchips.win_bet()
        if dealer_busts(dealer):
            print("\nThe dealer has gone bust, you win!")
            pchips.win_bet() 
        if dealer_wins(player , dealer):
            print("\nThe dealer has won, sorry.")
            pchips.lose_bet() 
        if push(player,dealer):
            print("\nYour hand is of equal value to the dealer's, it's  a draw!")
    
    print("Your number of chips:  " + str(pchips.total))
    
    # Ask to play again
    print("\n")
    x = True
    while x:
        y = input("Would you like to play again? Type 'y' for yes or 'n' for no.   ")
        if y[0].lower() == 'y':
            x = False
        elif y[0].lower() == 'n':
            x = False
        else:
            continue
    if y[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\n\nThanks for playing!")
        break