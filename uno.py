import random

def build_deck():
    """
    This function reutrn a deck of 108 cards
    Parameters: None
    Return values: card_Deck -> list
    """
    card_Deck = []
    deck_colours  = ["Red", "Green", "Yellow", "Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Skip", "Reverse", "Draw Two"]
    
    for colour in deck_colours:
        for value in values:
            cardVal = f"{colour} {value}"
            card_Deck.append(cardVal)

            if value != 0:
                card_Deck.append(cardVal)
 
    for i in range(4):
        card_Deck.append("wild")
        card_Deck.append("wild draw four")
    
    return card_Deck

deck = build_deck()

def shuffle_deck(deck):
    """
    This function shuffles the deck of cards
    Parameters: deck -> list
    Return: shuffled deck of cards -> list
    """
    random.shuffle(deck)
    shuffled_deck = deck
    random.shuffle(shuffled_deck)
    return shuffled_deck

shuffled_deck = shuffle_deck(deck)

def players():
    print("="*20, "Welcome to UNO, The 4 player card game!", "="*20)
    print("=="*40, "\n")
    numOf_players = int(input("How many players in the game?: "))
    if  numOf_players > 4 or numOf_players < 1:
        print("You need a minimum of 1 player and a maximum of 4 players")
    else:
        for player in range(numOf_players):
            print(f"Player {player} get ready to receive your hand")
        return numOf_players

players()
game_players = players()


